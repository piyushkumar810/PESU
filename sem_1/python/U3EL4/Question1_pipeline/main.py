# ✅ FIRST: THE QUESTION (Written Properly for Exam / Assignment)
# Question 1: Single Water Flow Sensor in a Household Pipeline
'''
A household pipeline is fitted with a single water flow sensor that continuously monitors water usage.
You are required to:

Context:-
One flow sensor monitors household water usage.
Simulation Requirements
Generate data for 48 hours
Sampling interval: 1 second
flow_lpm (liters per minute) should be 0 when idle
Inject usage bursts (tap usage, shower, washing machine)
Inject a slow water leak for 6 hours
Add sensor noise during flow

Pandas Tasks:-
Segment usage events using a flow threshold
Compute total water usage per hour
Detect leakage using sustained low flow
Classify usage patterns based on duration and intensity
Generate a leakage impact report
'''

# ------------------------------- solution
# PART 1: HOW TO THINK ABOUT THESE PROBLEMS
# These are SIMULATION + DATA ANALYSIS questions

'''
Real World Situation
        ↓
Simulated Sensor Data (Python)
        ↓
Pandas DataFrame
        ↓
Analysis + Detection + Report

'''

#!/usr/bin/env python3
"""
simulate_flow_analysis.py

Simulate a household water flow sensor (48 hours, 1s sampling),
analyze usage events, detect leaks, classify usage patterns, and
produce visualizations.

Usage:
    python simulate_flow_analysis.py

Outputs:
    - flow_events.csv            : detected usage events
    - leak_report.csv            : leakage impact report
    - hourly_usage.png           : bar chart of liters per hour
    - leak_zoom.png              : zoomed time-series around leak (or first 8 hours)
    - event_duration_hist.png    : histogram of usage durations (minutes)
    - duration_pie.png           : pie chart of duration classes
"""

from datetime import timedelta
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import random
import os

# ---------------------------
# Configuration (tweak here)
# ---------------------------
RANDOM_SEED = 42
START = pd.Timestamp("2026-01-01 00:00:00")
DURATION_HOURS = 48
SAMPLING_FREQ = 's'   # 's' means seconds
LEAK_START = START + pd.Timedelta(hours=3)
LEAK_DURATION_HOURS = 6
LEAK_BASE_LPM = 0.4

USAGE_THRESHOLD_LPM = 1.0   # >1 LPM considered "in use" event
LEAK_MIN_FLOW = 0.1         # detect low flow >= 0.1
LEAK_MAX_FLOW = 1.0         # detect low flow <= 1.0
LEAK_MIN_DURATION_HOURS = 2 # sustained low flow minimum to flag leak

OUTPUT_DIR = "flow_outputs"

# ---------------------------
# Helpers
# ---------------------------
def add_event(flow_arr, base_start, start_time, duration_s, base_flow_lpm, jitter=0.2):
    """
    Add a smooth event to flow_arr with sinusoidal rise/fall.
    flow_arr: numpy array (modified in-place)
    base_start: pd.Timestamp start used to compute seconds offset
    start_time: pd.Timestamp event start
    duration_s: seconds duration
    base_flow_lpm: peak scale (sin window multiplies it)
    jitter: noise std deviation
    """
    start_i = int((start_time - base_start).total_seconds())
    end_i = start_i + int(duration_s)
    if start_i < 0:
        start_i = 0
    if end_i > len(flow_arr):
        end_i = len(flow_arr)
    L = end_i - start_i
    if L <= 0:
        return
    t = np.linspace(0, math.pi, L)
    window = np.sin(t)  # 0..1..0 shape
    noise = np.random.normal(0, jitter, size=L)
    flow_arr[start_i:end_i] += np.maximum(0, base_flow_lpm * window + noise)

# ---------------------------
# Simulation
# ---------------------------
def simulate_flow(start=START, duration_hours=DURATION_HOURS, seed=RANDOM_SEED):
    """Return DataFrame indexed by timestamp with column 'flow_lpm'"""
    np.random.seed(seed)
    random.seed(seed)

    duration_seconds = int(duration_hours * 3600)
    index = pd.date_range(start=start, periods=duration_seconds, freq=SAMPLING_FREQ)
    n = len(index)
    flow = np.zeros(n, dtype=float)

    # Deterministic events each day
    for day in range(int(duration_hours / 24)):
        day_offset = pd.Timedelta(days=day)
        # Morning shower ~7:20 (10 min, ~10 LPM)
        add_event(flow, start, start + day_offset + pd.Timedelta(hours=7, minutes=20),
                  duration_s=10*60, base_flow_lpm=10, jitter=0.5)
        # Evening shower ~19:00 (12 min)
        add_event(flow, start, start + day_offset + pd.Timedelta(hours=19, minutes=0),
                  duration_s=12*60, base_flow_lpm=11, jitter=0.6)
        # Washing machine ~12:30 (40 min)
        add_event(flow, start, start + day_offset + pd.Timedelta(hours=12, minutes=30),
                  duration_s=40*60, base_flow_lpm=18, jitter=1.0)
        # Many small faucet taps during the day
        taps_count = 60
        for _ in range(taps_count):
            t_sec = random.randint(6*3600, 22*3600)
            add_event(flow, start, start + day_offset + pd.Timedelta(seconds=t_sec),
                      duration_s=random.randint(5, 60), base_flow_lpm=random.uniform(2.5, 6.0), jitter=0.5)
        # Toilet flushes (very short bursts)
        for _ in range(8):
            t_sec = random.randint(0, 24*3600-1)
            add_event(flow, start, start + day_offset + pd.Timedelta(seconds=t_sec),
                      duration_s=random.randint(3, 8), base_flow_lpm=random.uniform(6,9), jitter=0.3)

    # Inject leak (single block)
    add_event(flow, start, LEAK_START, duration_s=int(LEAK_DURATION_HOURS*3600), base_flow_lpm=LEAK_BASE_LPM, jitter=0.05)

    # Occasional random baseline noise (measurement quirks)
    noise_indices = np.random.choice(n, size=int(0.001 * n), replace=False)
    flow[noise_indices] += np.random.normal(0, 0.15, size=len(noise_indices))

    # Add sensor noise while flow > 0
    flow_noise = np.where(flow > 0, np.random.normal(0, 0.2, size=n), 0.0)
    flow += flow_noise
    flow = np.clip(flow, 0.0, None)

    df = pd.DataFrame({"flow_lpm": flow}, index=index)
    df.index.name = "timestamp"
    return df

# ---------------------------
# Analysis
# ---------------------------
def analyze_flow(df,
                 usage_threshold=USAGE_THRESHOLD_LPM,
                 leak_min_flow=LEAK_MIN_FLOW,
                 leak_max_flow=LEAK_MAX_FLOW,
                 leak_min_duration_h=LEAK_MIN_DURATION_HOURS):
    """
    Perform segmentation, hourly aggregation, leak detection, classification.
    Returns: events_df, hourly_usage (DataFrame), leaks_df, leak_report_df
    """
    # 1) Mark 'in_use' by threshold
    df = df.copy()
    df["in_use"] = df["flow_lpm"] > usage_threshold

    # assign segment ids for usage events (increment when in_use toggles from 0->1)
    df["segment_id"] = (df["in_use"].astype(int).diff() == 1).cumsum() * df["in_use"].astype(int)

    # gather segments
    segments = []
    for seg_id, seg in df[df["segment_id"] > 0].groupby("segment_id"):
        start_ts = seg.index[0]
        end_ts = seg.index[-1]
        duration_s = int((end_ts - start_ts).total_seconds()) + 1
        mean_flow = seg["flow_lpm"].mean()
        total_liters = (seg["flow_lpm"] / 60.0).sum()
        segments.append({
            "segment_id": int(seg_id),
            "start": start_ts,
            "end": end_ts,
            "duration_s": duration_s,
            "mean_flow_lpm": mean_flow,
            "total_liters": total_liters
        })
    events_df = pd.DataFrame(segments).sort_values("start").reset_index(drop=True) if segments else pd.DataFrame(
        columns=["segment_id","start","end","duration_s","mean_flow_lpm","total_liters"]
    )

    # 2) Hourly usage: convert LPM -> liters per second (divide by 60) then sum per hour
    df["liters_per_second"] = df["flow_lpm"] / 60.0
    hourly_usage = df["liters_per_second"].resample("1H").sum().rename("liters_per_hour").to_frame()

    # 3) Leak detection: sustained low flow in [leak_min_flow, leak_max_flow] for >= leak_min_duration_h
    low_flow_mask = (df["flow_lpm"] >= leak_min_flow) & (df["flow_lpm"] <= leak_max_flow)
    df["low_flow_seg"] = (low_flow_mask.astype(int).diff() == 1).cumsum() * low_flow_mask.astype(int)

    leak_candidates = []
    for seg_id, seg in df[df["low_flow_seg"] > 0].groupby("low_flow_seg"):
        start_ts = seg.index[0]
        end_ts = seg.index[-1]
        duration_s = int((end_ts - start_ts).total_seconds()) + 1
        avg_flow = seg["flow_lpm"].mean()
        total_liters = (seg["flow_lpm"] / 60.0).sum()
        if duration_s >= int(leak_min_duration_h * 3600):
            leak_candidates.append({
                "low_seg_id": int(seg_id),
                "start": start_ts,
                "end": end_ts,
                "duration_s": duration_s,
                "avg_flow_lpm": avg_flow,
                "total_liters": total_liters
            })
    leaks_df = pd.DataFrame(leak_candidates).sort_values("start").reset_index(drop=True) if leak_candidates else pd.DataFrame(
        columns=["low_seg_id","start","end","duration_s","avg_flow_lpm","total_liters"]
    )

    # 4) Classify usage events by duration and intensity
    def classify_event(row):
        dur = row["duration_s"]
        meanf = row["mean_flow_lpm"]
        # duration class
        if dur < 60:
            dur_class = "short"
        elif dur < 600:
            dur_class = "medium"
        else:
            dur_class = "long"
        # intensity class
        if meanf < 5:
            inten = "low"
        elif meanf < 12:
            inten = "medium"
        else:
            inten = "high"
        return pd.Series({"duration_class": dur_class, "intensity_class": inten})

    if not events_df.empty:
        events_df = pd.concat([events_df, events_df.apply(classify_event, axis=1)], axis=1)

    # 5) Leakage impact report
    total_consumption_liters = df["liters_per_second"].sum()
    leak_report = []
    for _, r in leaks_df.iterrows():
        leak_report.append({
            "start": r["start"],
            "end": r["end"],
            "duration_h": r["duration_s"] / 3600.0,
            "avg_flow_lpm": r["avg_flow_lpm"],
            "leaked_liters": r["total_liters"],
            "pct_of_total": 100.0 * r["total_liters"] / total_consumption_liters if total_consumption_liters > 0 else 0.0
        })
    leak_report_df = pd.DataFrame(leak_report) if leak_report else pd.DataFrame(
        columns=["start","end","duration_h","avg_flow_lpm","leaked_liters","pct_of_total"]
    )

    return df, events_df, hourly_usage, leaks_df, leak_report_df

# ---------------------------
# Plotting utilities
# ---------------------------
def plot_hourly_usage(hourly_usage, outpath):
    plt.figure(figsize=(12,5))
    hourly_usage.plot(kind="bar", legend=False)
    plt.title("Total water usage per hour (liters)")
    plt.xlabel("Hour (48h)")
    plt.ylabel("Liters per hour")
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()

def plot_zoom_leak(df, leaks_df, outpath, default_hours=8):
    if not leaks_df.empty:
        wstart = leaks_df.loc[0, "start"] - pd.Timedelta(hours=1)
        wend = leaks_df.loc[0, "end"] + pd.Timedelta(hours=1)
    else:
        wstart = df.index[0]
        wend = df.index[0] + pd.Timedelta(hours=default_hours)
    window_df = df.loc[wstart:wend]
    plt.figure(figsize=(12,4))
    plt.plot(window_df.index, window_df["flow_lpm"])
    plt.title("Flow (LPM) around detected leak period (zoomed)")
    plt.xlabel("Time")
    plt.ylabel("Flow (LPM)")
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()

def plot_event_duration_hist(events_df, outpath):
    if events_df.empty:
        return
    plt.figure(figsize=(8,4))
    durations_min = events_df["duration_s"] / 60.0
    plt.hist(durations_min, bins=30)
    plt.title("Distribution of usage event durations (minutes)")
    plt.xlabel("Duration (minutes)")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()

def plot_duration_pie(events_df, outpath):
    if events_df.empty:
        return
    plt.figure(figsize=(6,6))
    class_counts = events_df["duration_class"].value_counts()
    plt.pie(class_counts, labels=class_counts.index, autopct='%1.1f%%')
    plt.title("Usage event duration class share")
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()

# ---------------------------
# Main execution
# ---------------------------
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("Simulating flow data...")
    df = simulate_flow()
    print("Analyzing flow data...")
    df_analyzed, events_df, hourly_usage, leaks_df, leak_report_df = analyze_flow(df)

    # Summaries
    total_liters = df_analyzed["liters_per_second"].sum()
    print(f"Generated {len(df_analyzed)} samples. Total water used (48h): {total_liters:.2f} L")
    print(f"Detected usage events (> {USAGE_THRESHOLD_LPM} LPM): {len(events_df)}")
    print(f"Detected leak segments by rule: {len(leaks_df)}")

    # Save CSVs
    events_csv = os.path.join(OUTPUT_DIR, "flow_events.csv")
    leak_csv = os.path.join(OUTPUT_DIR, "leak_report.csv")
    hourly_csv = os.path.join(OUTPUT_DIR, "hourly_usage.csv")
    events_df.to_csv(events_csv, index=False)
    leak_report_df.to_csv(leak_csv, index=False)
    hourly_usage.to_csv(hourly_csv)
    print("Saved CSVs to", OUTPUT_DIR)

    # Plots
    plot_hourly_usage(hourly_usage, os.path.join(OUTPUT_DIR, "hourly_usage.png"))
    plot_zoom_leak(df_analyzed, leaks_df, os.path.join(OUTPUT_DIR, "leak_zoom.png"))
    plot_event_duration_hist(events_df, os.path.join(OUTPUT_DIR, "event_duration_hist.png"))
    plot_duration_pie(events_df, os.path.join(OUTPUT_DIR, "duration_pie.png"))
    print("Saved plots to", OUTPUT_DIR)

    # Print leak report summary if exists
    if not leak_report_df.empty:
        print("\nLeakage impact report (summary):")
        print(leak_report_df.to_string(index=False))
    else:
        print("\nNo leaks flagged by current rule. You can adjust LEAK_MIN_FLOW / LEAK_MAX_FLOW / LEAK_MIN_DURATION_HOURS.")

    print("\nDone. Check the 'flow_outputs' folder for CSVs and PNGs.")

if __name__ == "__main__":
    main()

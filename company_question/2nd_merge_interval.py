'''
Problem
Given an array of intervals where intervals[i] = [start, end], merge all overlapping intervals and 
return an array of the non-overlapping intervals.

Example:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
'''

# Approach
'''
Step 1: Sort the intervals
Sort by the start time.
[[1,3],[2,6],[8,10],[15,18]]

Step 2: Iterate
If the current interval overlaps with the last merged interval:
Update the end time.
Otherwise:
Add it as a new interval.
'''


# Python Solution
def merge(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]

        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return merged

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))
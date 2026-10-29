# ============================================
# COMPUTER VISION - KALMAN FILTER OBJECT TRACKING
# ============================================

import cv2
import numpy as np

# 1. Load video
cap = cv2.VideoCapture("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\PESU\\sem_3\\nlp\\important_coding_questions\\video_processing\\traffic_video.mp4")

if not cap.isOpened():
    print("Video not found!")
    exit()

# 2. Detect moving objects by comparing frames
# MOG2 separates moving foreground from background
background = cv2.createBackgroundSubtractorMOG2(
    history=300,
    varThreshold=40,
    detectShadows=False
)

# 3. Create Kalman Filter
# State: x, y, vx, vy
# Measurement: x, y
kalman = cv2.KalmanFilter(4, 2)

# State transition matrix
kalman.transitionMatrix = np.array([
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
], dtype=np.float32)

# Measurement matrix: measure only x and y
kalman.measurementMatrix = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0]
], dtype=np.float32)

# Process and measurement uncertainty
kalman.processNoiseCov = np.eye(4, dtype=np.float32) * 0.03
kalman.measurementNoiseCov = np.eye(2, dtype=np.float32) * 1.0
kalman.errorCovPost = np.eye(4, dtype=np.float32)

initialized = False

while True:
    # 4. Read one video frame
    ret, frame = cap.read()

    if not ret:
        break

    # 5. Detect moving regions
    mask = background.apply(frame)

    # Remove small noise
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(
        mask, cv2.MORPH_OPEN, kernel
    )

    # 6. Find moving-object contours
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Ignore tiny moving regions
    valid_contours = [
        c for c in contours
        if cv2.contourArea(c) > 500
    ]

    measurement = None

    if valid_contours:
        # Select the largest detected moving region
        largest = max(valid_contours, key=cv2.contourArea)

        x, y, w, h = cv2.boundingRect(largest)

        # Calculate object's center
        center_x = x + w // 2
        center_y = y + h // 2

        measurement = np.array([
            [np.float32(center_x)],
            [np.float32(center_y)]
        ])

        # Draw measured position and bounding box
        cv2.rectangle(
            frame, (x, y), (x + w, y + h),
            (0, 255, 0), 2
        )

        cv2.circle(
            frame, (center_x, center_y),
            5, (0, 255, 0), -1
        )

    # 7. Initialize filter from the first measurement
    if not initialized and measurement is not None:
        kalman.statePost = np.array([
            [measurement[0, 0]],
            [measurement[1, 0]],
            [0],
            [0]
        ], dtype=np.float32)

        initialized = True

    # 8. Predict the next position
    if initialized:
        prediction = kalman.predict()

        pred_x = int(prediction[0, 0])
        pred_y = int(prediction[1, 0])

        cv2.circle(
            frame, (pred_x, pred_y),
            6, (0, 0, 255), -1
        )

        # 9. Correct prediction if measurement exists
        if measurement is not None:
            corrected = kalman.correct(measurement)

            corr_x = int(corrected[0, 0])
            corr_y = int(corrected[1, 0])

            cv2.circle(
                frame, (corr_x, corr_y),
                5, (255, 0, 0), -1
            )

        cv2.putText(
            frame, "Green: Measurement",
            (10, 25), cv2.FONT_HERSHEY_SIMPLEX,
            0.6, (0, 255, 0), 2
        )

        cv2.putText(
            frame, "Red: Prediction",
            (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
            0.6, (0, 0, 255), 2
        )

        cv2.putText(
            frame, "Blue: Corrected estimate",
            (10, 75), cv2.FONT_HERSHEY_SIMPLEX,
            0.6, (255, 0, 0), 2
        )

    # 10. Display output
    cv2.imshow("Kalman Object Tracking", frame)
    cv2.imshow("Moving Object Mask", mask)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

# 11. Release resources
cap.release()
cv2.destroyAllWindows()
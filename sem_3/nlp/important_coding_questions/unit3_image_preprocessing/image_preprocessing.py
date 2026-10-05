# ============================================
# COMPUTER VISION - IMAGE PROCESSING PRACTICAL
# ============================================

import cv2
import numpy as np
from pathlib import Path


# --------------------------------------------
# 1. Load Image
# --------------------------------------------

base_dir = Path(__file__).resolve().parent
image_path = base_dir / "cinamatic_image.jpeg"

image = cv2.imread(str(image_path))

if image is None:
    print(f"Image not found: {image_path}")
    exit()

print(f"Image loaded successfully from: {image_path}")


# --------------------------------------------
# 2. Display Original Image
# --------------------------------------------

cv2.imshow("Original Image", image)


# --------------------------------------------
# 3. Resizing
# --------------------------------------------

resized = cv2.resize(image, (500, 500))

cv2.imshow("Resized Image", resized)


# --------------------------------------------
# 4. Grayscale
# --------------------------------------------

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Grayscale Image", gray)


# --------------------------------------------
# 5. Gaussian Blur
# --------------------------------------------

gaussian_blur = cv2.GaussianBlur(
    image,
    (5, 5),
    0
)

cv2.imshow("Gaussian Blur", gaussian_blur)


# --------------------------------------------
# 6. Median Blur
# --------------------------------------------

median_blur = cv2.medianBlur(
    image,
    5
)

cv2.imshow("Median Blur", median_blur)


# --------------------------------------------
# 7. Normalization
# --------------------------------------------

normalized = cv2.normalize(
    gray,
    None,
    0,
    255,
    cv2.NORM_MINMAX
)

cv2.imshow("Normalized Image", normalized)


# --------------------------------------------
# 8. Contrast Enhancement
# --------------------------------------------

# Convert image to grayscale
gray_contrast = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)

# Improve contrast using Histogram Equalization
contrast = cv2.equalizeHist(gray_contrast)
# MCQ:-  it always takes gray scale image only

cv2.imshow("Contrast Enhanced", contrast)


# --------------------------------------------
# 9. Cropping
# --------------------------------------------

# Image format:
# image[y1:y2, x1:x2]

cropped = image[100:400, 100:400]

cv2.imshow("Cropped Image", cropped)


# --------------------------------------------
# 10. Rotation - 45 Degrees
# --------------------------------------------

height, width = image.shape[:2]

center = (width // 2, height // 2)

rotation_matrix = cv2.getRotationMatrix2D(
    center,
    45,
    1.0
)

rotated = cv2.warpAffine(
    image,
    rotation_matrix,
    (width, height)
)

cv2.imshow("Rotated 45 Degrees", rotated)


# --------------------------------------------
# 11. Horizontal Flip
# --------------------------------------------

horizontal_flip = cv2.flip(
    image,
    1
)

cv2.imshow("Horizontal Flip", horizontal_flip)


# --------------------------------------------
# 12. Vertical Flip
# --------------------------------------------

vertical_flip = cv2.flip(
    image,
    0
)

cv2.imshow("Vertical Flip", vertical_flip)


# --------------------------------------------
# 13. Save Processed Images
# --------------------------------------------

cv2.imwrite(base_dir / "resized.jpg", resized)
cv2.imwrite(base_dir / "grayscale.jpg", gray)
cv2.imwrite(base_dir / "gaussian_blur.jpg", gaussian_blur)
cv2.imwrite(base_dir / "median_blur.jpg", median_blur)
cv2.imwrite(base_dir / "normalized.jpg", normalized)
cv2.imwrite(base_dir / "contrast.jpg", contrast)
cv2.imwrite(base_dir / "cropped.jpg", cropped)
cv2.imwrite(base_dir / "rotated.jpg", rotated)
cv2.imwrite(base_dir / "horizontal_flip.jpg", horizontal_flip)
cv2.imwrite(base_dir / "vertical_flip.jpg", vertical_flip)


# --------------------------------------------
# 14. Wait and Close Windows
# --------------------------------------------

cv2.waitKey(0)
cv2.destroyAllWindows()
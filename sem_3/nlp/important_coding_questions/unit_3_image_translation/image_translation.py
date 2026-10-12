
# ==========================================
# COMPUTER VISION - IMAGE TRANSFORMATION
# ==========================================

import cv2
import numpy as np

# 1. Load image
image = cv2.imread("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\PESU\\sem_3\\nlp\\important_coding_questions\\unit_3_image_translation\\world-map.map.gif")

if image is None:
    print("Image not found!")
    exit()

height, width = image.shape[:2]
# print(height, width)

cv2.imshow("Original Image", image)


# ==========================================
# 2. TRANSLATION - MOVE IMAGE
# ==========================================

tx = 100
ty = 50

# Matrix shifts image right by 100 and down by 50
translation_matrix = np.float32([
    [1, 0, tx],
    [0, 1, ty]
])

translated = cv2.warpAffine(
    image, translation_matrix, (width, height)
)

cv2.imshow("Translation", translated)

# MCQ: Translation matrix is 2x3 in OpenCV.
# Positive tx = right; positive ty = down.


# ==========================================
# 3. SCALING - RESIZE IMAGE
# ==========================================

scaled = cv2.resize(image, None, fx=2, fy=2)

cv2.imshow("Scaling", scaled)

# MCQ:
# fx = horizontal scale factor
# fy = vertical scale factor
# fx=2, fy=2 doubles width and height.
# Scaling around the origin can be different from
# scaling around the image center.


# ==========================================
# 4. ROTATION - ROTATE BY 45 DEGREES
# ==========================================

center = (width // 2, height // 2)

rotation_matrix = cv2.getRotationMatrix2D(
    center, 45, 1.0
)

rotated = cv2.warpAffine(
    image, rotation_matrix, (width, height)
)

cv2.imshow("Rotation 45 Degrees", rotated)

# MCQ:
# getRotationMatrix2D(center, angle, scale)
# Positive angle = counter-clockwise rotation
# in the usual OpenCV coordinate convention.


# ==========================================
# 5. HORIZONTAL SHEARING
# ==========================================

shx = 0.5

horizontal_shear_matrix = np.float32([
    [1, shx, 0],
    [0, 1, 0]
])

horizontal_shear = cv2.warpAffine(
    image, horizontal_shear_matrix, (width, height)
)

cv2.imshow("Horizontal Shearing", horizontal_shear)

# MCQ: x' = x + shx*y; y' = y.
# Horizontal shear changes the x-coordinate.


# ==========================================
# 6. VERTICAL SHEARING
# ==========================================

shy = 0.5

vertical_shear_matrix = np.float32([
    [1, 0, 0],
    [shy, 1, 0]
])

vertical_shear = cv2.warpAffine(
    image, vertical_shear_matrix, (width, height)
)

cv2.imshow("Vertical Shearing", vertical_shear)

# MCQ: x' = x; y' = y + shy*x.
# Vertical shear changes the y-coordinate.


# ==========================================
# 7. AFFINE TRANSFORMATION
# ==========================================

# Select three points from the original image.
source_points = np.float32([
    [50, 50],
    [200, 50],
    [50, 200]
])

# Specify where those points should move.
destination_points = np.float32([
    [10, 100],
    [200, 80],
    [100, 250]
])

# Three point pairs determine a 2D affine transform.
affine_matrix = cv2.getAffineTransform(
    source_points, destination_points
)

affine = cv2.warpAffine(
    image, affine_matrix, (width, height)
)

cv2.imshow("Affine Transformation", affine)

# MCQ:
# getAffineTransform() uses 3 corresponding point pairs.
# warpAffine() applies the 2x3 transformation matrix.
# Affine transformations preserve straight lines
# and parallelism.


# ==========================================
# 8. SAVE TRANSFORMED IMAGES
# ==========================================

cv2.imwrite("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\PESU\\sem_3\\nlp\\important_coding_questions\\unit_3_image_translation\\translated.jpg", translated)
cv2.imwrite("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\PESU\\sem_3\\nlp\\important_coding_questions\\unit_3_image_translation\\scaled.jpg", scaled)
cv2.imwrite("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\PESU\\sem_3\\nlp\\important_coding_questions\\unit_3_image_translation\\rotated.jpg", rotated)
cv2.imwrite("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\PESU\\sem_3\\nlp\\important_coding_questions\\unit_3_image_translation\\horizontal_shear.jpg", horizontal_shear)
cv2.imwrite("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\PESU\\sem_3\\nlp\\important_coding_questions\\unit_3_image_translation\\vertical_shear.jpg", vertical_shear)
cv2.imwrite("C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\PESU\\sem_3\\nlp\\important_coding_questions\\unit_3_image_translation\\affine.jpg", affine)

# imwrite() saves an image to disk.


# ==========================================
# 9. CLOSE WINDOWS
# ==========================================

cv2.waitKey(0)
cv2.destroyAllWindows()

# waitKey(0) waits until a key is pressed.
# destroyAllWindows() closes all OpenCV windows.

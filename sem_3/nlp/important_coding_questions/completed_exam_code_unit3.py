# COMPUTER VISION - IMAGE PROCESSING ASSIGNMENTS (Q1-Q33)
# Install first: python -m pip install opencv-python numpy matplotlib
# Put image.jpg in the same folder as this file.
# Run the file and enter a question number (1-33), or 0 to run all.
#
# OpenCV color images use BGR; Matplotlib color images use RGB.

import cv2
import numpy as np
import matplotlib.pyplot as plt

IMAGE_PATH = "image.jpg"
image = cv2.imread(IMAGE_PATH)
if image is None:
    raise FileNotFoundError(
        f"Cannot find {IMAGE_PATH}. Put image.jpg beside this .py file "
        "or change IMAGE_PATH to the correct path."
    )

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def to_rgb(img):
    """Convert OpenCV BGR color image to RGB for Matplotlib."""
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def show_one(title, img, gray=False):
    """Display one image."""
    plt.imshow(img, cmap="gray" if gray else None)
    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.show()


def show_grid(items, columns=3, figsize=(13, 8)):
    """items contains (title, image, is_grayscale) tuples."""
    rows = (len(items) + columns - 1) // columns
    plt.figure(figsize=figsize)
    for i, (title, img, is_gray) in enumerate(items):
        plt.subplot(rows, columns, i + 1)
        plt.imshow(img, cmap="gray" if is_gray else None)
        plt.title(title)
        plt.axis("off")
    plt.tight_layout()
    plt.show()


# Q1. Read and display the original image using Matplotlib.
def q1():
    # Matplotlib expects RGB, so display image_rgb rather than OpenCV's BGR image.
    show_one("Q1 - Original Image", image_rgb)


# Q2. Convert a color image to grayscale.
def q2():
    # BGR2GRAY converts a 3-channel BGR image to a single-channel grayscale image.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    show_one("Q2 - Grayscale", gray, gray=True)


# Q3. Improve grayscale contrast using histogram equalization.
def q3():
    # equalizeHist requires an 8-bit, single-channel grayscale image.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(gray)
    show_grid([("Grayscale", gray, True), ("Equalized", equalized, True)], columns=2)


# Q4. Resize to 224 x 224 pixels.
def q4():
    # cv2.resize uses (width, height), not (height, width).
    resized = cv2.resize(image, (224, 224))
    show_one("Q4 - Resize 224x224", to_rgb(resized))


# Q5. Crop the central portion.
def q5():
    h, w = image.shape[:2]  # h = height/rows; w = width/columns.

    # Image slicing is [y_start:y_end, x_start:x_end].
    # h//4 = one-quarter height; 3*h//4 = three-quarters height.
    # w//4 = one-quarter width; 3*w//4 = three-quarters width.
    # So this keeps the middle half of the image in both dimensions.
    # // means integer (floor) division.
    cropped = image[h//4:3*h//4, w//4:3*w//4]
    show_one("Q5 - Center Crop", to_rgb(cropped))


# Q6. Flip horizontally.
def q6():
    # flipCode=1 mirrors left-to-right.
    flipped = cv2.flip(image, 1)
    show_one("Q6 - Horizontal Flip", to_rgb(flipped))


# Q7. Rotate 90 degrees clockwise.
def q7():
    # The built-in rotate constant specifies a 90-degree clockwise rotation.
    rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    show_one("Q7 - 90 Degrees Clockwise", to_rgb(rotated))


# Q8. Enlarge by factor 1.5.
def q8():
    # fx scales width; fy scales height. 1.5 means 150% of the original size.
    enlarged = cv2.resize(image, None, fx=1.5, fy=1.5)
    show_one("Q8 - Scale 1.5x", to_rgb(enlarged))


# Q9. Translate 50 pixels right and 30 down using warpAffine.
def q9():
    h, w = image.shape[:2]
    # Translation matrix: tx=50 (right); ty=30 (down).
    M = np.float32([[1, 0, 50], [0, 1, 30]])
    # Output canvas size is (width, height).
    translated = cv2.warpAffine(image, M, (w, h))
    show_one("Q9 - Right 50, Down 30", to_rgb(translated))


# Q10. Rotate 90 degrees clockwise using cv2.rotate().
def q10():
    # Same operation as Q7; the assignment asks for it separately.
    rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    show_one("Q10 - 90 Degrees Clockwise", to_rgb(rotated))


# Q11. Enlarge 1.5x along x and y axes.
def q11():
    # fx=1.5 scales width/x; fy=1.5 scales height/y.
    scaled = cv2.resize(image, None, fx=1.5, fy=1.5)
    show_one("Q11 - Scale 1.5x", to_rgb(scaled))


# Q12. Apply a 21x21 average filter.
def q12():
    # cv2.blur replaces each pixel with the mean of its 21x21 neighborhood.
    average = cv2.blur(image, (21, 21))
    show_one("Q12 - Average Filter 21x21", to_rgb(average))


# Q13. Apply Gaussian blur with a 21x21 kernel.
def q13():
    # GaussianBlur weights nearby pixels according to a Gaussian distribution.
    # sigmaX=0 lets OpenCV calculate sigma from the kernel size.
    gaussian = cv2.GaussianBlur(image, (21, 21), 0)
    show_one("Q13 - Gaussian Blur 21x21", to_rgb(gaussian))


# Q14. Apply median filter with kernel size 21.
def q14():
    # Median replaces each pixel with the neighborhood's median value.
    # Kernel size must be an odd integer greater than 1.
    median = cv2.medianBlur(image, 21)
    show_one("Q14 - Median Blur 21", to_rgb(median))


# Q15. Show original, average, Gaussian, and median-filtered images.
def q15():
    average = cv2.blur(image, (21, 21))
    gaussian = cv2.GaussianBlur(image, (21, 21), 0)
    median = cv2.medianBlur(image, 21)
    show_grid([
        ("Original", image_rgb, False),
        ("Average 21x21", to_rgb(average), False),
        ("Gaussian 21x21", to_rgb(gaussian), False),
        ("Median 21", to_rgb(median), False)
    ], columns=2)


# Q16. Detect vertical edges using Sobel X.
def q16():
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # dx=1, dy=0 calculates intensity change along x; often highlights vertical edges.
    # CV_64F preserves negative and positive derivative values.
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    # convertScaleAbs takes absolute values and converts the result to 8-bit.
    sobel_x = cv2.convertScaleAbs(sobel_x)
    show_one("Q16 - Sobel X / Vertical Edges", sobel_x, gray=True)


# Q17. Detect horizontal edges using Sobel Y.
def q17():
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # dx=0, dy=1 calculates intensity change along y; often highlights horizontal edges.
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel_y = cv2.convertScaleAbs(sobel_y)
    show_one("Q17 - Sobel Y / Horizontal Edges", sobel_y, gray=True)


# Q18. Detect edges using the Laplacian operator.
def q18():
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Laplacian uses second-order derivatives to highlight intensity changes.
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    laplacian = cv2.convertScaleAbs(laplacian)
    show_one("Q18 - Laplacian Edges", laplacian, gray=True)


# Q19. Display Sobel X, Sobel Y, and Laplacian side by side.
def q19():
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sx = cv2.convertScaleAbs(cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3))
    sy = cv2.convertScaleAbs(cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3))
    lap = cv2.convertScaleAbs(cv2.Laplacian(gray, cv2.CV_64F))
    show_grid([("Sobel X", sx, True), ("Sobel Y", sy, True),
               ("Laplacian", lap, True)], columns=3)


# Q20. Convert to grayscale and apply Sobel X, Sobel Y, and Laplacian.
def q20():
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sx = cv2.convertScaleAbs(cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3))
    sy = cv2.convertScaleAbs(cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3))
    lap = cv2.convertScaleAbs(cv2.Laplacian(gray, cv2.CV_64F))
    show_grid([("Grayscale", gray, True), ("Sobel X", sx, True),
               ("Sobel Y", sy, True), ("Laplacian", lap, True)], columns=2)


# Q21. Display original, grayscale, and histogram-equalized images.
def q21():
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(gray)
    show_grid([("Original", image_rgb, False), ("Grayscale", gray, True),
               ("Equalized", equalized, True)], columns=3)


# Q22. Perform cropping, horizontal flipping, and resizing.
def q22():
    h, w = image.shape[:2]
    # Keep the middle half: [y_start:y_end, x_start:x_end].
    cropped = image[h//4:3*h//4, w//4:3*w//4]
    flipped = cv2.flip(image, 1)
    resized = cv2.resize(image, (224, 224))
    show_grid([("Center Crop", to_rgb(cropped), False),
               ("Horizontal Flip", to_rgb(flipped), False),
               ("Resize 224x224", to_rgb(resized), False)], columns=3)


# Q23. Perform translation, rotation, and scaling.
def q23():
    h, w = image.shape[:2]
    # Positive tx moves right; positive ty moves down.
    M = np.float32([[1, 0, 50], [0, 1, 30]])
    translated = cv2.warpAffine(image, M, (w, h))
    # Rotate 45 degrees about the center; scale factor 1.0 means same size.
    R = cv2.getRotationMatrix2D((w//2, h//2), 45, 1.0)
    rotated = cv2.warpAffine(image, R, (w, h))
    scaled = cv2.resize(image, None, fx=1.5, fy=1.5)
    show_grid([("Translation", to_rgb(translated), False),
               ("Rotation 45 Degrees", to_rgb(rotated), False),
               ("Scaling 1.5x", to_rgb(scaled), False)], columns=3)


# Q24. Compare average, Gaussian, and median filtering.
def q24():
    average = cv2.blur(image, (21, 21))
    gaussian = cv2.GaussianBlur(image, (21, 21), 0)
    median = cv2.medianBlur(image, 21)
    show_grid([("Original", image_rgb, False),
               ("Average", to_rgb(average), False),
               ("Gaussian", to_rgb(gaussian), False),
               ("Median", to_rgb(median), False)], columns=2)


# Q25. Full pipeline: preprocessing, manipulation, transformation,
# filtering, and edge detection.
def q25():
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(image, (224, 224))
    flipped = cv2.flip(image, 1)

    h, w = image.shape[:2]
    M = np.float32([[1, 0, 50], [0, 1, 30]])
    translated = cv2.warpAffine(image, M, (w, h))
    R = cv2.getRotationMatrix2D((w//2, h//2), 45, 1.0)
    rotated = cv2.warpAffine(image, R, (w, h))

    average = cv2.blur(image, (5, 5))
    gaussian = cv2.GaussianBlur(image, (5, 5), 0)
    median = cv2.medianBlur(image, 5)

    sx = cv2.convertScaleAbs(cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3))
    sy = cv2.convertScaleAbs(cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3))
    lap = cv2.convertScaleAbs(cv2.Laplacian(gray, cv2.CV_64F))

    show_grid([
        ("Original", image_rgb, False), ("Grayscale", gray, True),
        ("Resized", to_rgb(resized), False), ("Horizontal Flip", to_rgb(flipped), False),
        ("Translation", to_rgb(translated), False), ("Rotation", to_rgb(rotated), False),
        ("Average Filter", to_rgb(average), False), ("Gaussian Blur", to_rgb(gaussian), False),
        ("Median Blur", to_rgb(median), False), ("Sobel X", sx, True),
        ("Sobel Y", sy, True), ("Laplacian", lap, True)
    ], columns=4, figsize=(15, 10))


# Q26. Rotate the image by 180 degrees.
def q26():
    rotated = cv2.rotate(image, cv2.ROTATE_180)
    show_one("Q26 - Rotate 180 Degrees", to_rgb(rotated))


# Q27. Flip vertically instead of horizontally.
def q27():
    # flipCode=0 mirrors top-to-bottom.
    flipped = cv2.flip(image, 0)
    show_one("Q27 - Vertical Flip", to_rgb(flipped))


# Q28. Move 100 pixels left and 50 pixels upward.
def q28():
    h, w = image.shape[:2]
    # Negative tx moves left; negative ty moves up.
    M = np.float32([[1, 0, -100], [0, 1, -50]])
    translated = cv2.warpAffine(image, M, (w, h))
    show_one("Q28 - Left 100, Up 50", to_rgb(translated))


# Q29. Double the image size.
def q29():
    # fx=2 doubles width and fy=2 doubles height.
    doubled = cv2.resize(image, None, fx=2, fy=2)
    show_one("Q29 - Double Size", to_rgb(doubled))


# Q30. Compare average filter sizes 21x21 and 5x5.
def q30():
    # Larger kernels generally produce stronger blur.
    avg5 = cv2.blur(image, (5, 5))
    avg21 = cv2.blur(image, (21, 21))
    show_grid([("Original", image_rgb, False), ("Average 5x5", to_rgb(avg5), False),
               ("Average 21x21", to_rgb(avg21), False)], columns=3)


# Q31. Apply a 3x3 average filter.
def q31():
    average = cv2.blur(image, (3, 3))
    show_one("Q31 - Average Filter 3x3", to_rgb(average))


# Q32. Detect edges with Sobel and convertScaleAbs().
def q32():
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Sobel X calculates intensity change in x direction.
    sobel = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    # convertScaleAbs takes absolute values and converts to 8-bit for display.
    result = cv2.convertScaleAbs(sobel)
    show_one("Q32 - Sobel X", result, gray=True)


# Q33. Display several image-processing results in a grid.
def q33():
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(image, (224, 224))
    flipped = cv2.flip(image, 1)
    gaussian = cv2.GaussianBlur(image, (5, 5), 0)
    median = cv2.medianBlur(image, 5)
    sobel = cv2.convertScaleAbs(cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3))

    show_grid([
        ("Original", image_rgb, False), ("Grayscale", gray, True),
        ("Resized", to_rgb(resized), False), ("Horizontal Flip", to_rgb(flipped), False),
        ("Gaussian Blur", to_rgb(gaussian), False), ("Median Blur", to_rgb(median), False),
        ("Sobel X", sobel, True)
    ], columns=4, figsize=(13, 7))


# Choose a question number to run only that solution.
# Enter 0 to run all 33 questions one after another.
QUESTIONS = {
    1: q1, 2: q2, 3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 8: q8, 9: q9,
    10: q10, 11: q11, 12: q12, 13: q13, 14: q14, 15: q15, 16: q16,
    17: q17, 18: q18, 19: q19, 20: q20, 21: q21, 22: q22, 23: q23,
    24: q24, 25: q25, 26: q26, 27: q27, 28: q28, 29: q29, 30: q30,
    31: q31, 32: q32, 33: q33
}

if __name__ == "__main__":
    print("Computer Vision - Image Processing Assignments")
    print("Enter 1-33 to run one question, or 0 to run all questions.")
    choice = int(input("Question number: "))

    if choice == 0:
        for number, function in QUESTIONS.items():
            print(f"Running Question {number}...")
            function()
    elif choice in QUESTIONS:
        QUESTIONS[choice]()
    else:
        print("Invalid choice. Enter a number from 0 to 33.")

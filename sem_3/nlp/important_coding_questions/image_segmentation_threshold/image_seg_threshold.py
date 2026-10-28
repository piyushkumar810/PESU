import cv2
import matplotlib.pyplot as plt

# Read the image in grayscale
img = cv2.imread(
    'C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\PESU\\sem_3\\nlp\\important_coding_questions\\image_segmentation_threshold\\scaled.jpg',
    cv2.IMREAD_GRAYSCALE
)

# # Apply binary thresholding
# ret, result = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# # Display the images
# plt.figure(figsize=(12, 4))

# plt.subplot(1, 2, 1)
# plt.imshow(img, cmap='gray')
# plt.title('Original Grayscale Image')
# plt.axis('off')

# plt.subplot(1, 2, 2)
# plt.imshow(result, cmap='gray')
# plt.title('Binary Threshold Image')
# plt.axis('off')

# plt.tight_layout()
# plt.show()


# convert RGB to gray scale
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

result=img.copy()

mask=cv2.UMat(1,1,cv2.CV_8UC1)

seed_point=(200,150)

cv2.floodFill(
    result,None,seed_point,(0,255,0),
    loDiff=(20,20,20),
    upDiff=(20,20,20)
)


# Convert result to RGB for display
result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

# Display images
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(result_rgb,cv2.COLOR_BGR2RGB))
plt.title('Flood Fill Segmentation')
plt.axis('off')

plt.tight_layout()
plt.show()
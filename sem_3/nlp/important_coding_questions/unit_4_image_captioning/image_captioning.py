
# ============================================================
# IMAGE CAPTION GENERATION USING BLIP MODEL
# ============================================================

# Step 0: Install required libraries
# Run this separately if libraries are not installed
'''pip install transformers torch torchvision pillow'''

# Step 1: Import required components from Hugging Face
from transformers import BlipProcessor, BlipForConditionalGeneration

# Step 2: Import PIL to open and display images
from PIL import Image

# Step 3: Load the pretrained BLIP processor
# It prepares the image in the format required by the model
processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

# Step 4: Load the pretrained BLIP model
# This model generates captions for images
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

# Step 5: Load an image
# Replace this path with your actual image path
image_path = "C:\\Users\\piyush kumar\\OneDrive\\Desktop\\GitHub\\PESU\\sem_3\\nlp\\important_coding_questions\\unit3_image_preprocessing\\cinamatic_image.jpeg"

image = Image.open(image_path).convert("RGB")

# Step 6: Display the original image
display(image)

# Step 7: Process the image
# Convert the image into tensors that the model understands
inputs = processor(image, return_tensors="pt")

# Step 8: Generate a caption
# The model predicts the most suitable description
out = model.generate(**inputs, max_new_tokens=50)

# Step 9: Convert generated token IDs into readable text
caption = processor.decode(out[0], skip_special_tokens=True)

# Step 10: Display the generated caption
image.show()
print("Generated Image Caption:", caption)















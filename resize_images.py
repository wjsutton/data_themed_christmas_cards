
from PIL import Image
import os

# Define the desired size
desired_size = (1748, 2480)

# Directory paths
input_directory = 'card_designs'
output_directory = 'resized_images'

# Ensure output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Loop through each image in the input directory
for filename in os.listdir(input_directory):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        image_path = os.path.join(input_directory, filename)
        img = Image.open(image_path)

        # Determine the scale needed to reach the desired dimension while maintaining aspect ratio
        original_aspect = img.width / img.height
        new_aspect = desired_size[0] / desired_size[1]

        # Check if the image needs to be resized based on the aspect ratio
        if original_aspect > new_aspect:
            # The image is wider than the target aspect, so scale by height and then crop width
            scale_factor = desired_size[1] / img.height
        else:
            # The image is taller than the target aspect, so scale by width and then crop height
            scale_factor = desired_size[0] / img.width

        # Resize the image
        img_resized = img.resize((int(img.width * scale_factor), int(img.height * scale_factor)), Image.ANTIALIAS)

        # Center-crop the image to the desired aspect ratio
        left = (img_resized.width - desired_size[0]) / 2
        top = (img_resized.height - desired_size[1]) / 2
        right = (img_resized.width + desired_size[0]) / 2
        bottom = (img_resized.height + desired_size[1]) / 2

        img_cropped = img_resized.crop((left, top, right, bottom))

        # Save the cropped image with a unique name
        resized_cropped_image_path = os.path.join(output_directory, f'resized_{filename}')
        img_cropped.save(resized_cropped_image_path)

        print(f'Processed {filename}')

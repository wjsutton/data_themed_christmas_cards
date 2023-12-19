
from fpdf import FPDF
import os

# Define the A5 size dimensions
A5_WIDTH_IN_MM = 148
A5_HEIGHT_IN_MM = 210

# Directory path
input_directory = 'resized_images'
postcard_output_directory = 'blank_postcards'
folding_card_output_directory = 'blank_folding_cards'

# Ensure output directories exist
if not os.path.exists(postcard_output_directory):
    os.makedirs(postcard_output_directory)

if not os.path.exists(folding_card_output_directory):
    os.makedirs(folding_card_output_directory)

# Loop through each image in the input directory
for filename in os.listdir(input_directory):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        image_path = os.path.join(input_directory, filename)

        # Initialize PDFs
        postcard_pdf = FPDF(unit="mm", format="A5")
        postcard_pdf.add_page()
        folding_card_pdf = FPDF(unit="mm", format="A5")
        folding_card_pdf.add_page()

        # Add image to Postcard PDF
        postcard_pdf.add_page()  # Second for image
        postcard_pdf.image(image_path, x=0, y=0, w=A5_WIDTH_IN_MM, h=A5_HEIGHT_IN_MM)
        postcard_output = os.path.join(postcard_output_directory, f'postcard_{filename}.pdf')
        postcard_pdf.output(postcard_output)

        # Add image to Folding Card PDF
        folding_card_pdf.add_page()  # Second for image
        folding_card_pdf.image(image_path, x=0, y=0, w=A5_WIDTH_IN_MM, h=A5_HEIGHT_IN_MM)
        folding_card_pdf.add_page()  # Third blank page
        folding_card_pdf.add_page()  # Fourth blank page
        folding_card_output = os.path.join(folding_card_output_directory, f'folding_card_{filename}.pdf')
        folding_card_pdf.output(folding_card_output)

        print(f'Processed {filename}')

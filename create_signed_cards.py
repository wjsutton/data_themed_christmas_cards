
from fpdf import FPDF
import pandas as pd
import random
import os

# Define the A5 size dimensions
A5_WIDTH_IN_MM = 148
A5_HEIGHT_IN_MM = 210

# Greeting messages
greetings_messages = [
    "Holiday joy in every data point! Wishing you an off-the-charts Happy New Year!",
    "Merry data visualizations and a bright, error-free New Year!",
    "Warm holidays, happy memories, and error-free New Year's data backups!",
    "Joining tables with loved ones this season. Happy, efficient New Year!",
    "Season's Greetings! Wishing you outlier-free joy and positive correlations in the New Year!"
]

# Directory paths
input_directory = 'resized_images'
postcard_output_directory = 'signed_postcards'
folding_card_output_directory = 'signed_folding_cards'

# Ensure output directories exist
if not os.path.exists(postcard_output_directory):
    os.makedirs(postcard_output_directory)

if not os.path.exists(folding_card_output_directory):
    os.makedirs(folding_card_output_directory)

# Read names from CSV file
csv_path = 'card_list.csv'
names_df = pd.read_csv(csv_path)

for name in names_df['Name']:
    # Select a random card design
    card_designs = [f for f in os.listdir(input_directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
    random_design = random.choice(card_designs)
    image_path = os.path.join(input_directory, random_design)

    # Generate postcard
    postcard_pdf = FPDF(unit="mm", format="A5")
    postcard_pdf.add_page()  # Greetings page
    # Add greeting text
    postcard_pdf.set_font("Arial", size=18)
    postcard_pdf.set_xy(10, 10)
    postcard_pdf.cell(0, 10, f"Dear {name}", ln=True)
    postcard_pdf.set_font("Arial", size=26, style='B')
    postcard_pdf.set_xy(0, 95)
    postcard_pdf.multi_cell(0, 10, random.choice(greetings_messages), align='C')
    postcard_pdf.set_font("Arial", size=18)
    postcard_pdf.set_xy(-40, 170)
    postcard_pdf.cell(0, 10, "From Will", ln=True, align='R')
    # Add image
    postcard_pdf.add_page()
    postcard_pdf.image(image_path, x=0, y=0, w=A5_WIDTH_IN_MM, h=A5_HEIGHT_IN_MM)
    # Save postcard
    postcard_output = os.path.join(postcard_output_directory, f'postcard_{name}.pdf')
    postcard_pdf.output(postcard_output)

    # Generate folding card
    folding_card_pdf = FPDF(unit="mm", format="A5")
    folding_card_pdf.add_page()
    folding_card_pdf.add_page()  # Second page image
    folding_card_pdf.image(image_path, x=0, y=0, w=A5_WIDTH_IN_MM, h=A5_HEIGHT_IN_MM)
    folding_card_pdf.add_page()  # Third blank page
    folding_card_pdf.add_page()  # Greetings page
    # Add greeting text
    folding_card_pdf.set_font("Arial", size=18)
    folding_card_pdf.set_xy(10, 10)
    folding_card_pdf.cell(0, 10, f"Dear {name}", ln=True)
    folding_card_pdf.set_font("Arial", size=26, style='B')
    folding_card_pdf.set_xy(0, 95)
    folding_card_pdf.multi_cell(0, 10, random.choice(greetings_messages), align='C')
    folding_card_pdf.set_font("Arial", size=18)
    folding_card_pdf.set_xy(-40, 170)
    folding_card_pdf.cell(0, 10, "From Will", ln=True, align='R')
    # Save folding card
    folding_card_output = os.path.join(folding_card_output_directory, f'folding_card_{name}.pdf')
    folding_card_pdf.output(folding_card_output)

    print(f'Created card for {name}')

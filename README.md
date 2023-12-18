# Data-Themed Seasons Greetings Cards Generator

<p align="center">
  <img src="resized_images/resized_design1.png" width="30%" />
  <img src="resized_images/resized_design2.png" width="20%" />
  <img src="resized_images/resized_design3.png" width="30%" />
  <img src="resized_images/resized_design4.png" width="30%" />
  <img src="resized_images/resized_design5.png" width="30%" />
  <img src="resized_images/resized_design6.png" width="30%" />
</p>


## Introduction
This project is designed to create personalized seasons greetings cards with a data-themed twist. Users can easily modify the theme to fit their preferences. The project generates two types of greeting cards - postcards and folding cards - both in A5 size. These can be printed double-sided for physical distribution.

## Project Structure
- `card_designs/`: Folder containing the initial card designs.
- `resized_images/`: Folder where resized images are saved.
- `scripts/`:
  - `resize_images.py`: Script to resize images to A5 size.
  - `create_blank_cards.py`: Script to create blank cards for editing and personalization.
  - `create_signed_cards.py`: Script to create signed cards with a personalized message using a CSV file of names.

## Images

These images have been created using Dalle-3 via ChatGPT-4. The following prompts were used to create the images:

- Can you design for me 4 data themed Christmas / seasons greetings cards, remove any text, and size them as 1748 x 2480 pixels
- Could I have 4 more card designs, themed on people coming together over the holidays with data, sized 1748 x 2480 pixels, with no text
- Could I have 4 more card designs, themed on the holidays with data, sized 1748 x 2480 pixels, with no text, no humans

After each prompt I would select the design I liked or ask ChatGPT to redraw ones that had noticable issues. 

Of note the sizing for 1748 x 2480 pixels was regularly not applied, hence why the script to `resize_images/py` was produced. 

## Usage
### Resizing Images
1. Place your card design images in the `card_designs/` folder.
2. Run `resize_images.py` to resize these images to A5 size. The resized images will be saved in `resized_images/`.

### Creating Blank Cards
Run `create_blank_cards.py` to generate blank cards. This script produces two types of cards:
- Postcards: 2 A5 pages.
- Folding Cards: 4 A5 pages.

### Creating Signed Cards
1. To create signed cards with personalized messages, first prepare a CSV file with the names of the recipients.
2. Edit the `create_signed_cards.py` script to customize the greeting messages.
3. Run `create_signed_cards.py`. This will generate signed cards, each containing one of the names from the CSV file.

## Customization
Users can customize the design of the cards by replacing images in `card_designs/` and modifying the greeting messages in the `create_signed_cards.py` script.

## Requirements
- Python 3
- Libraries: FPDF, PIL, pandas

## Installation
1. Clone the repository or download the project files.
2. Install the required Python libraries:
   ```
   pip install fpdf Pillow pandas
   ```

## Running the Scripts
Navigate to the project directory and run the scripts as follows:
```
python resize_images.py
python create_blank_cards.py
python create_signed_cards.py
```

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License
[MIT License](LICENSE)


# Image Processing Project 📷

## Overview
This repository contains a collection of scripts and tools designed for image processing. 
The project is built to handle various image transformations, manipulations, and analyses, 
leveraging Python and powerful image-processing libraries.

## Features
- **Image Filters**: Apply various filters (e.g., grayscale, blur, edge detection).
- **Resizing and Cropping**: Easily resize and crop images.
- **Image Transformation**: Perform rotation, scaling, and other transformations.
- **Format Conversion**: Convert images to different formats (e.g., JPG to PNG).
- **Batch Processing**: Process multiple images simultaneously.
- **Custom Filters**: Add your custom filters and processing algorithms.

## Prerequisites

### Tools & Environment
- Python 3.7 or later.
- A virtual environment is recommended for managing dependencies.

### Libraries
Install the required libraries using pip:
```bash
pip install -r requirements.txt
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/josuesmoody/Image-Processesing-Project.git
cd Image-Processesing-Project
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Running Image Processing Scripts
The scripts are modular and can be executed individually. For example:
```bash
python scripts/apply_filter.py --input ./images/input.jpg --output ./images/output.jpg --filter grayscale
```

### Batch Processing
You can use the `batch_process.py` script for processing multiple images in a directory:
```bash
python scripts/batch_process.py --input_dir ./images/input/ --output_dir ./images/output/ --operation resize --size 256x256
```

### Adding Custom Functions
You can add custom filters or transformations by modifying the `custom_filters.py` script.

## Directory Structure
```
Image-Processesing/
├── images/                 # Directory for input and output images
├── scripts/                # Scripts for specific image processing tasks
│   ├── apply_filter.py     # Apply filters to images
│   ├── resize_crop.py      # Resize and crop images
│   ├── batch_process.py    # Script for batch image processing
│   └── custom_filters.py   # Define custom filters here
├── requirements.txt        # Dependencies list
├── README.md               # Project documentation
└── LICENSE                 # License file
```

## Key Technologies Used

- **OpenCV**: For efficient image manipulation and analysis.
- **NumPy**: For numerical computations.
- **Pillow (PIL)**: For image file operations.
- **Argparse**: For creating command-line interfaces.

## Contributing

Contributions are welcome! If you'd like to improve or add features:
1. Fork this repository.
2. Create a new branch for your changes.
3. Test thoroughly and submit a pull request.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more details.

## Acknowledgments

- Inspired by the flexibility of Python in handling image processing.
- Powered by the vibrant open-source community.

## Contact

Created by **Josué Elías Santana**.  
Feel free to [contact me](https://www.linkedin.com/in/josue-santana/) for any inquiries.

---
✨ Enjoy transforming images and unleashing creativity! ✨

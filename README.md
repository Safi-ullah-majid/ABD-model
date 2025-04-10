# ABD-model: Atom and Bond Detection Model

This repository contains a model for detecting atoms and bonds in molecular images. It can be used for various applications in molecular chemistry and image analysis.

## Overview

The **ABD-model** is a deep learning-based model designed to detect atoms (e.g., C, O, H, N) and bond types (single, double, triple) in molecular structure images. The model can be used to extract information from 2D molecular representations and convert it into useful data for further computational chemistry analysis.

## Features

- **Atom detection**: Detects atoms like Carbon, Oxygen, Nitrogen, and Hydrogen in molecular images.
- **Bond detection**: Identifies single, double, and triple bonds between atoms.
- **Versatility**: Works with a wide variety of molecular structure images.
- **Open-source**: Easy to integrate into your own projects and customize.

## Requirements

To run this model, you need to install the following dependencies:

- Python 3.x
- PyTorch (or TensorFlow, depending on your implementation)
- OpenCV (for image processing)
- NumPy
- Any other libraries listed in `requirements.txt`

To install the dependencies, run:

```bash
pip install -r requirements.txt

# ABD Model

This repository contains a trained YOLO model for detecting atoms and bonds in handwritten molecular structure images.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Safi-ullah-majid/ABD-model.git
   cd ABD-model

2.  Install dependencie
 pip install -r requirements.txt
3. Download the model file (ABD.pt) and make sure it’s in the correct directory.
Usage
To make predictions using the model, run the predict.py script:

bash
Copy
Edit
python predict.py --input_path path/to/image
Ensure that the model is loaded correctly and that the input image is a valid image file.
License
This repository is licensed under the MIT License - see the LICENSE file for details.

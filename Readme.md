# RGB-to-XYZ Image Conversion Script

## Overview

This Python script performs color space transformations between the **RGB** and **CIE XYZ** color spaces. Using the **Pillow** library, it processes an input image, applies transformations using the provided matrices, and outputs intermediate results for analysis.

Find more information about RGB-XYZ space conversion on : 
'''
https://en.wikipedia.org/wiki/CIE_1931_color_space#CIE_RGB_color_space
'''
## Usage

Before running the script, make sure you have the following installed:

   `Python 3.x`

To run the script, follow these steps:

1. Clone the repository to your local machine:
```bash
   git clone https://github.com/xdarksoul/RGBconverter.git
```
2. Install the required packages:
```bash
   pip install Pillow
```
3. Navigate to the project directory:

```bash
   cd RGBconverter
```
4. Run the script:

```bash
   python main.py
```

## Matrix Formulas

RGB to XYZ Transformation Matrix:
```
[[0.412453 0.357580 0.180423]
 [0.212671 0.715160 0.072169]
 [0.019334 0.119193 0.950227]]

```
XYZ to RGB Transformation Matrix:
```
[[ 3.24048134 -1.53715152 -0.49853633]
 [-0.96925495  1.87599  0.04155593]
 [ 0.05564664 -0.20404134  1.05731107]]

```

## Input/Output Files
The script takes an input image file and outputs the following files:
 
Input:
 - `parrots.bmp`

Output:
- `original_rgb.txt`   # Pixel values of individual RGB channels
- `rgb2xyz.txt`        # Pixel values of XYZ channels after RGB to XYZ transformation
- `xyz2rgb.txt`        # Pixel values of RGB channels after XYZ to RGB transformation
- `xyz2rgb.jpg`        # Output image after XYZ to RGB transformation


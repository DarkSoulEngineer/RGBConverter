# RGBConverter
**A Python script that converts images between RGB and XYZ color spaces using matrix transformations.**

[![License: GPL v3](https://img.shields.io/github/license/DarkSoulEngineer/RGBConverter)](LICENSE)
![Python](https://img.shields.io/badge/language-Python%203.x-3776AB)

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Matrix Formulas](#matrix-formulas)
- [Input/Output Files](#inputoutput-files)
- [License](#license)

## Description

RGBConverter is a Python script that performs color space transformations between the **RGB** and **CIE XYZ** color spaces. Using the **Pillow** library, it processes an input image, applies transformations with the matrices defined in the script, and writes the intermediate pixel data to text files for analysis.

For background on the conversion, see the [CIE 1931 color space](https://en.wikipedia.org/wiki/CIE_1931_color_space#CIE_RGB_color_space) article on Wikipedia.

## Requirements

- **Python 3.x**
- **Pillow**

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/DarkSoulEngineer/RGBConverter.git
   cd RGBConverter
   ```

2. Install the required package:

   ```bash
   pip install Pillow
   ```

## Usage

Run the script from the project directory:

```bash
python main.py
```

When prompted, enter the name of an image file in the project directory (for example, `parrots.bmp`). The script will convert the image and generate the output files described below.

## Matrix Formulas

RGB to XYZ transformation matrix (CIE RGB, as defined in `main.py`):
```
[[ 0.4868870  0.3062984  0.1710347]
 [ 0.1746583  0.8247541  0.0005877]
 [-0.0012563  0.0169832  0.8094831]]
```

XYZ to RGB transformation matrix (CIE RGB, as defined in `main.py`):
```
[[ 2.3638081 -0.8676030 -0.4988161]
 [-0.5005940  1.3962369  0.1047562]
 [ 0.0141712 -0.0306400  1.2323842]]
```

## Input/Output Files

The script takes an input image file and outputs the following files:

Input:
- `parrots.bmp` — sample image included in the repository

Output:
- `original_rgb.txt`   # Pixel values of individual RGB channels
- `rgb2xyz.txt`        # Pixel values of XYZ channels after RGB to XYZ transformation
- `xyz2rgb.txt`        # Pixel values of RGB channels after XYZ to RGB transformation
- `xyz2rgb.jpg`        # Output image after XYZ to RGB transformation

## License

GPL-3.0 — see [LICENSE](LICENSE).

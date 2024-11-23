#!/usr/bin/env python3

# import Image processing lib. 
from PIL import Image

def main():

    # Matrix for rgb2xyz CIE RGB
    rgb2xyz = (
         0.4868870,  0.3062984,  0.1710347, 0,
        0.1746583,  0.8247541, 0.0005877, 0,
        -0.0012563,  0.0169832,  0.8094831, 0)

    # Matrix for xyz2rgb CIE RGB
    xyz2rgb = (
        2.3638081, -0.8676030, -0.4988161, 0,
        -0.5005940,  1.3962369,  0.1047562, 0,
        0.0141712, -0.0306400,  1.2323842, 0)

    # Get user input -- image_name
    image_name = input("Enter file name: ")

    # Open image from input'
    im = Image.open(image_name)  

    # Write {image_name} pixels(RGB) to original_rgb.txt
    with open("original_rgb.txt","w") as f:
        for pix in im.getdata():
            f.write(f"{pix}")
        f.close()

    # Convert image to rgb2xyz
    xyz = im.convert("RGB", rgb2xyz)

    # Write xyz(converted image rgb2xyz) pixels(RGB) to rgb2xyz.txt
    with open("rgb2xyz.txt","w") as f:
        for pix in xyz.getdata():
            f.write(f"{pix}")
        f.close()

    # Convert image to original 
    rgb = xyz.convert("RGB", xyz2rgb)

    # Write rgb(converted image xyz2rgb) pixels(RGB) to xyz2rgb.txt
    with open("xyz2rgb.txt","w") as f:
        for pix in rgb.getdata():
            f.write(f"{pix}")     
        f.close()

    # Save xyz2rgb image as xyz2rgb.jpg 
    rgb.save("xyz2rgb.jpg")

if __name__ == "__main__":
    main()
    
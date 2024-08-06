"""
File: fire.py
Name: 劉庭宇
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage

HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: SimpleImage, the file that contains a sate image of a fire
    :return: SimpleImage, red are set to 255 of where the fire is and gray scale for places without fire
    """
    img = SimpleImage(filename)  # define image
    for pixel in img:  # for every pixel in the image
        avg = (pixel.red + pixel.blue + pixel.green) // 3  # define average value
        if pixel.red > avg * HURDLE_FACTOR:  # for every red pixel if bigger than avg*THRESHOLD, change into red=255
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:  # turning all other pixels into grayscale
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return img


def main():
    """
    ---Algo---
    1. commands from assignment
    2. call out highlighted_fire function
    3. show original image & show processed image
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

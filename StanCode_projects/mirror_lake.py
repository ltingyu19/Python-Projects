"""
File: mirror_lake.py
Name: 劉庭宇
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: SimpleImage, image of an background
    :return: SimpleImage, image of the original image, but mirrored vertically
    """

    img = SimpleImage(filename)  # read original file
    mir_img = SimpleImage.blank(img.width, img.height * 2) # define a new image with blank background and specific
    # resolution

    # for each x and y coordinates of the original picture
    for x in range(img.width):
        for y in range(img.height):
            img_pixel = img.get_pixel(x, y)  # define pixel element
            mir_img_pixel = mir_img.get_pixel(x, y)

            mir_img_pixel.red = img_pixel.red  # pixel element of mirrored image == original picture's pixel element
            mir_img_pixel.green = img_pixel.green
            mir_img_pixel.blue = img_pixel.blue

            # the pixels of the mirrored part of the image is defined in manner that y is counted inversely,
            mir_img_pixel2 = mir_img.get_pixel(x, mir_img.width - 1 - y)
            mir_img_pixel2.red = img_pixel.red
            mir_img_pixel2.green = img_pixel.green
            mir_img_pixel2.blue = img_pixel.blue

    return mir_img  # return mirrored image


def main():
    """
   ---Algo---
    1. commands from assignment
    2. call out reflected function to process mirroring action
    3. show original image & show processed image
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

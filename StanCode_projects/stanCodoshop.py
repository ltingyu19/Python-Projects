"""
File: stanCodoshop.py
Name: 劉庭宇
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage

# In order to use "sqrt", math has been imported
import math


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """

    # Defines the mathematical equation of color distance and returns as float
    color_dist = math.sqrt((red - pixel.red) ** 2 + (green - pixel.green) ** 2 + (blue - pixel.blue) ** 2)
    return float(color_dist)


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """

    # Define variables and list
    tot_red = 0
    tot_green = 0
    tot_blue = 0
    avg_colors = []

    # To read all pixels and add them up
    for i in range(len(pixels)):
        pixel = pixels[i]
        tot_red += pixel.red
        tot_green += pixel.green
        tot_blue += pixel.blue

    # With total pixel value ready, avg pixel value is calculated, using the length of list
    avg_red = tot_red // len(pixels)
    avg_green = tot_green // len(pixels)
    avg_blue = tot_blue // len(pixels)

    # Adding pixel average value to new list defined as "avg_colors"
    avg_colors.append(avg_red)
    avg_colors.append(avg_green)
    avg_colors.append(avg_blue)

    return avg_colors


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """

    # With previous defined functions, define average value of pixels
    avg_pixel = get_average(pixels)

    # Define minimum distance and iteration as two major reference for "for loops" below
    min_dist = 0
    iteration = 0

    # For every pixel in the list imported, we will calculate its color distance value and accumulate the value of
    # iteration
    for pixel in pixels:
        dist = get_pixel_dist(pixel, avg_pixel[0], avg_pixel[1], avg_pixel[2])
        iteration += 1
        # If iteration value is one, it means there are min_dist & best_pixel value still zero, so first iteration
        # values should be set to min/best value
        if iteration == 1:
            min_dist = dist
            best_pixel = pixel

        # If iteration is bigger than zero, it will need to compare with current values and eventaully selecting the
        # best pixel that we need
        else:
            if dist < min_dist:
                min_dist = dist
                best_pixel = pixel

    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)

    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect

    # -- Algo --
    # read and make a list for all the pixels
    # process them with get best pixel

    # Get all pixels
    for x in range(result.width):
        for y in range(result.height):

            # Define result pixel and list of pixel storage (saving the pixels we want to process)
            result_pixel = result.get_pixel(x, y)
            pixel_storage = []

            # for every pixel(x,y), we will now read multiple images and get different values for that specific pixel
            # we will then add it to the list we previously defined

            for image in images:
                image_pixel = image.get_pixel(x, y)
                pixel_storage.append(image_pixel)
                # ex. [pixel1 from img 1,pixel2 from img 2,pixel3 from img 3]

            # Process these pixels with previously defined functions and add them to the result image
            best_pixel = get_best_pixel(pixel_storage)
            result_pixel.red = best_pixel.red
            result_pixel.green = best_pixel.green
            result_pixel.blue = best_pixel.blue

    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()

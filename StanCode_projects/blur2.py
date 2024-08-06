"""
File: blur.py
Name: 劉庭宇
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, smiley face input
    :return: SimpleImage, blurred version of input image
    """
    # Define a new image
    new_img = SimpleImage.blank(img.width, img.height)

    # With double "for loop" to loop over original picture
    for x in range(img.width):
        for y in range(img.height):

            # set red, green, blue value of pixels sum == 0
            red_sum = 0
            green_sum = 0
            blue_sum = 0
            runs = 0

            # This is a special double loop for finding neighbors in a matrix
            # with "pixel_x/y_adapt", when i==-1, it finds all neighbors on left side
            # when i==0, it find up and down neighbors
            # when i==1, it finds all neighbors on right side
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    pixel_X_adapt = x + i
                    pixel_Y_adapt = y + j

                    # The two "if statement" is to make sure "pixel_x/y_adapt" doesn't go beyond pixel boundary of img
                    if 0 <= pixel_X_adapt < img.width:
                        if 0 <= pixel_Y_adapt < img.height:
                            # for every pixel, find sum of rgb value and collect runs(how many neighbors)
                            # if pixel is at the edge of img, runs != pixel in the middle
                            img_pixel = img.get_pixel(pixel_X_adapt, pixel_Y_adapt)
                            red_sum = red_sum + img_pixel.red
                            green_sum = green_sum + img_pixel.green
                            blue_sum = blue_sum + img_pixel.blue
                            runs = runs + 1

            # define blurred img's(nbew_image) rgb value with sums divided by runs(neighbors)
            new_img_pixel = new_img.get_pixel(x, y)
            new_img_pixel.red = red_sum / runs
            new_img_pixel.green = green_sum / runs
            new_img_pixel.blue = blue_sum / runs

    return new_img


def main():
    """
    ---Algo---
    1. commands from assignment
    2. call out blurring function to process the image
    3. show original image & show processed image
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()

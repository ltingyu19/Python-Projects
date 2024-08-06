"""
File: blur.py
Name:
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, smiley face input
    :return: SimpleImage, blurred version of input image
    """
    # Todo: create a new blank img that is as big as the original one

    new_img = SimpleImage.blank(img.width, img.height)


    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):

            img_pixel = img.get_pixel(x,y)
            new_img_pixel = new_img.get_pixel(x,y)

            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.

            if x == 0 and y == 0:
                # Get pixel at the top-left corner of the image.

                # Define image pixel around designated pixel element with x,y coordinates
                # add R,G,B element together and divide by int ＂number of neighbors +1" to get avg R,G,B value
                # designate avg R,G,B value for new the current element
                ### all functions below are written in this manner ###

                img_pixel_rightmiddle = img.get_pixel(x+1, y)
                img_pixel_rightdown = img.get_pixel(x+1, y+1)
                img_pixel_directdown = img.get_pixel(x, y+1)
                img_pixel = img.get_pixel(x, y)

                avg_red = (img_pixel_rightmiddle.red + img_pixel_rightdown.red + img_pixel_directdown.red+img_pixel.red) //4
                avg_green = (img_pixel_rightmiddle.green + img_pixel_rightdown.green + img_pixel_directdown.green+img_pixel.green) //4
                avg_blue = (img_pixel_rightmiddle.blue + img_pixel_rightdown.blue + img_pixel_directdown.blue+img_pixel.blue) //4

                new_img_pixel.red = avg_red
                new_img_pixel.green = avg_green
                new_img_pixel.blue = avg_blue


            elif x == img.width-1 and y == 0:
                # Get pixel at the top-right corner of the image.
                img_pixel_leftmiddle = img.get_pixel(x - 1, y)
                img_pixel_lefttdown = img.get_pixel(x - 1, y + 1)
                img_pixel_directdown = img.get_pixel(x, y + 1)
                img_pixel = img.get_pixel(x, y)

                avg_red = (img_pixel_leftmiddle.red + img_pixel_lefttdown.red + img_pixel_directdown.red+img_pixel.red) // 4
                avg_green = (img_pixel_leftmiddle.green + img_pixel_lefttdown.green + img_pixel_directdown.green+img_pixel.green) // 4
                avg_blue = (img_pixel_leftmiddle.blue + img_pixel_lefttdown.blue + img_pixel_directdown.blue+img_pixel.blue) // 4

                new_img_pixel.red = avg_red
                new_img_pixel.green = avg_green
                new_img_pixel.blue = avg_blue

            elif x == 0 and y == img.height-1:
                # Get pixel at the bottom-left corner of the image
                img_pixel_rightmiddle = img.get_pixel(x+1, y)
                img_pixel_rightup = img.get_pixel(x+1, y-1)
                img_pixel_directup = img.get_pixel(x, y-1)
                img_pixel = img.get_pixel(x, y)

                avg_red = (img_pixel_rightmiddle.red + img_pixel_rightup.red + img_pixel_directup.red+img_pixel.red) //4
                avg_green = (img_pixel_rightmiddle.green + img_pixel_rightup.green + img_pixel_directup.green+img_pixel.green) //4
                avg_blue = (img_pixel_rightmiddle.blue + img_pixel_rightup.blue + img_pixel_directup.blue+img_pixel.blue) //4

                new_img_pixel.red = avg_red
                new_img_pixel.green = avg_green
                new_img_pixel.blue = avg_blue

            elif x == img.width-1 and y == img.height-1:
                # Get pixel at the bottom-right corner of the image
                img_pixel_leftmiddle = img.get_pixel(x - 1, y)
                img_pixel_lefttup = img.get_pixel(x - 1, y - 1)
                img_pixel_directup = img.get_pixel(x, y - 1)
                img_pixel = img.get_pixel(x, y)

                avg_red = (img_pixel_leftmiddle.red + img_pixel_lefttup.red + img_pixel_directup.red+img_pixel.red) // 4
                avg_green = (img_pixel_leftmiddle.green + img_pixel_lefttup.green + img_pixel_directup.green+img_pixel.green) // 4
                avg_blue = (img_pixel_leftmiddle.blue + img_pixel_lefttup.blue + img_pixel_directup.blue+img_pixel.blue) // 4

                new_img_pixel.red = avg_red
                new_img_pixel.green = avg_green
                new_img_pixel.blue = avg_blue

            elif 0 < x < img.width-1 and y == 0:
                # Get top edge's pixels (without two corners)
                img_pixel_leftmiddle = img.get_pixel(x - 1, y)
                img_pixel_leftdown = img.get_pixel(x - 1, y + 1)
                img_pixel_directdown = img.get_pixel(x, y + 1)
                img_pixel_rightmiddle = img.get_pixel(x + 1, y)
                img_pixel_rightdown = img.get_pixel(x + 1, y + 1)
                img_pixel = img.get_pixel(x, y)

                avg_red = (img_pixel_leftmiddle.red + img_pixel_leftdown.red + img_pixel_directdown.red + img_pixel_rightmiddle.red + img_pixel_rightdown.red+img_pixel.red) // 6
                avg_green = (img_pixel_leftmiddle.green + img_pixel_leftdown.green + img_pixel_directdown.green + img_pixel_rightmiddle.red + img_pixel_rightdown.red +img_pixel.green) // 6
                avg_blue = (img_pixel_leftmiddle.blue + img_pixel_leftdown.blue + img_pixel_directdown.blue + img_pixel_rightmiddle.red + img_pixel_rightdown.red+img_pixel.blue) // 6

                new_img_pixel.red = avg_red
                new_img_pixel.green = avg_green
                new_img_pixel.blue = avg_blue

            elif 0 < x < img.width-1 and y == img.height-1:
                # Get bottom edge's pixels (without two corners)
                img_pixel_leftmiddle = img.get_pixel(x - 1, y)
                img_pixel_leftup = img.get_pixel(x - 1, y - 1)
                img_pixel_directup = img.get_pixel(x, y - 1)
                img_pixel_rightmiddle = img.get_pixel(x + 1, y)
                img_pixel_rightup = img.get_pixel(x + 1, y - 1)
                img_pixel = img.get_pixel(x, y)

                avg_red = (img_pixel_leftmiddle.red + img_pixel_leftup.red + img_pixel_directup.red + img_pixel_rightmiddle.red + img_pixel_rightup.red+img_pixel.red) // 6
                avg_green = (img_pixel_leftmiddle.green + img_pixel_leftup.green + img_pixel_directup.green + img_pixel_rightmiddle.red + img_pixel_rightup.red +img_pixel.green) // 6
                avg_blue = (img_pixel_leftmiddle.blue + img_pixel_leftup.blue + img_pixel_directup.blue + img_pixel_rightmiddle.red + img_pixel_rightup.red+img_pixel.blue) // 6

                new_img_pixel.red = avg_red
                new_img_pixel.green = avg_green
                new_img_pixel.blue = avg_blue

            elif x == 0 and 0 < y < img.height-1:
                # Get left edge's pixels (without two corners)
                img_pixel_rightmiddle = img.get_pixel(x+1, y)
                img_pixel_rightup = img.get_pixel(x+1, y - 1)
                img_pixel_directup = img.get_pixel(x, y - 1)
                img_pixel_directdown = img.get_pixel(x, y+1)
                img_pixel_rightdown = img.get_pixel(x + 1, y + 1)
                img_pixel = img.get_pixel(x, y)

                avg_red = ( img_pixel_directdown.red + img_pixel_rightdown.red + img_pixel_directup.red + img_pixel_rightmiddle.red + img_pixel_rightup.red+img_pixel.red) // 6
                avg_green = (img_pixel_directdown.green + img_pixel_rightdown.green + img_pixel_directup.green + img_pixel_rightmiddle.red + img_pixel_rightup.red+img_pixel.green) // 6
                avg_blue = (img_pixel_directdown.blue + img_pixel_rightdown.blue + img_pixel_directup.blue + img_pixel_rightmiddle.red + img_pixel_rightup.red+img_pixel.blue) // 6

                new_img_pixel.red = avg_red
                new_img_pixel.green = avg_green
                new_img_pixel.blue = avg_blue

            elif x == img.width-1 and 0 < y < img.height-1:
                # Get right edge's pixels (without two corners)
                img_pixel_leftmiddle = img.get_pixel(x-1, y)
                img_pixel_lefttup = img.get_pixel(x-1, y - 1)
                img_pixel_directup = img.get_pixel(x, y - 1)
                img_pixel_directdown = img.get_pixel(x, y+1)
                img_pixel_lefttdown = img.get_pixel(x - 1, y + 1)
                img_pixel = img.get_pixel(x, y)

                avg_red = ( img_pixel_leftmiddle.red + img_pixel_lefttup.red + img_pixel_directup.red + img_pixel_directdown.red + img_pixel_lefttdown.red+img_pixel.red) // 6
                avg_green = (img_pixel_leftmiddle.green + img_pixel_lefttup.green + img_pixel_directup.green + img_pixel_directdown.red + img_pixel_lefttdown.red+img_pixel.green) // 6
                avg_blue = (img_pixel_leftmiddle.blue + img_pixel_lefttup.blue + img_pixel_directup.blue + img_pixel_directdown.red + img_pixel_lefttdown.red+img_pixel.blue) // 6

                new_img_pixel.red = avg_red
                new_img_pixel.green = avg_green
                new_img_pixel.blue = avg_blue

            else:
                # Inner pixels.
                img_pixel_leftmiddle = img.get_pixel(x-1, y)
                img_pixel_lefttup = img.get_pixel(x-1, y - 1)
                img_pixel_lefttdown = img.get_pixel(x - 1, y + 1)
                img_pixel_directup = img.get_pixel(x, y - 1)
                img_pixel_directdown = img.get_pixel(x, y+1)
                img_pixel = img.get_pixel(x,y)
                img_pixel_righttup = img.get_pixel(x+1, y - 1)
                img_pixel_righttdown = img.get_pixel(x + 1, y + 1)
                img_pixel_rightmiddle = img.get_pixel(x+1, y)

                avg_red = (img_pixel_leftmiddle.red + img_pixel_lefttup.red + img_pixel_directup.red + img_pixel_directdown.red + img_pixel_lefttdown.red + img_pixel_rightmiddle.red +img_pixel_righttup.red + img_pixel_righttdown.red+img_pixel.red) // 9
                avg_green = (img_pixel_leftmiddle.green + img_pixel_lefttup.green + img_pixel_directup.green + img_pixel_directdown.green + img_pixel_lefttdown.green+img_pixel_rightmiddle.green +img_pixel_righttup.green + img_pixel_righttdown.green+img_pixel.green) // 9
                avg_blue = (img_pixel_leftmiddle.blue + img_pixel_lefttup.blue + img_pixel_directup.blue + img_pixel_directdown.blue  + img_pixel_lefttdown.blue +img_pixel_rightmiddle.blue  +img_pixel_righttup.blue  + img_pixel_righttdown.blue +img_pixel.blue) // 9

                new_img_pixel.red = avg_red
                new_img_pixel.green = avg_green
                new_img_pixel.blue = avg_blue

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


if __name__ == '__main__':
    main()

# Image manipulation

hueshift.py:

This program takes in a number that is used to manipulate the RGB values in the given image. In this implementation, there are two core functions. The first converts from RGB to HSV, a color space in which colors are arranged around the radius of a cone with lightness and saturation controlled by the theoretical coordinates within the cone. This gives us direct access to the hue value of each pixel. The second function converts HSV back into RGB, which is what the picture module uses.

dottify.py:

This program samples and pixelates an image into a grid of colored circles.

reduction.py:

An alternative pixelation program that breaks up the image into proportional rectangles and colors them based on the average color within the grid.

wavy.py:

Uses a sin function to offset the image and make it quite wavy based on user input


"""
Created By Hamish Robb in March 2019
Last Updated 5/25/2021
---------------------------------
||**||**|| wavy.py ||**||**||
---------------------------------
Args: (int) amplitude, (int) wavelength, (string) file name
---------------------------------
Desc: this program takes an image and applies a sine function
on the x and y coordinates of each pixel. the amplitude is the
actual displacement factor, and the wavelength controls how
tightly bound or wide the waves are in the final image

Concession: if i were to rebuild this from scratch, i would define
the sine function within a lambda that gets applied to each row of
pixels using Python 3's map(). it's more efficient and elegant, but
functional programming does not work with Picture2.
"""
import sys
import math
import picture2


# USAGE: a utility function to handle printing and quitting
def usage():
    print("Usage: python3 wavy.py [amplitude] [wavelength] (opt.)[filename]")
    sys.exit()


# WAVY:
# handles arguments and opens an image
# calculates a sine function with the
# user-specified args, outputs a wavy image
def wavy(argv):
    if (len(argv) < 3 or len(argv) > 4):
        print("Error: incorrect number of arguments")
        usage()
    img_file = "cat.bmp" if len(argv) == 3 else argv[2]
    amplitude = 0
    try:
        amplitude = int(sys.argv[1])
        wave_len = int(sys.argv[2])
    except:
        print("Error: one or more of the numbers given were invalid")
        usage()
    pic = None
    # try block 2: open file from args or default pic
    try:
        pic = picture2.Picture(img_file)
    except:
        print("Error: unable to open the specified file")
        usage()
    width = pic.getWidth()
    height = pic.getHeight()
    newpic = picture2.Picture(width, height)
    amplitude %= height
    for i in range(0, width):
        for j in range(0, height):
            r, g, b = pic.getPixelColor(i, j)
            offset = int(round(amplitude*math.sin(1/wave_len*i)))
            j += offset
            if j >= height:
                j -= height
            if j < 0:
                j += height
            newpic.setPixelColor(i, j, r, g, b)
    newpic.display()
    input("Press any key to exit: ")


if __name__ == "__main__":
    wavy(sys.argv)

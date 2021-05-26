"""
Created By Hamish Robb in March 2019
Last Updated 5/25/2021
---------------------------------
||**||**|| hueshift.py ||**||**||
---------------------------------
Args: (int) shift_number, (string) file_name
---------------------------------
Desc: this program takes an image and performs a conversion from
rgb (red, green, blue) colorspace to hsv (hue, saturation, value). then,
it takes a user-given number and shifts the hue of the hsv represented
image. lastly, it converts the image back to rgb and displays it
"""
import sys
import picture2


# RGB_TO_HSV:
# takes three integer values representing the rgb color values of a picture
# performs a conversion to hsv color space
# returns a tuplet of 3 integers
def rgb_to_hsv(r, g, b):
    ro = r/255.0
    go = g/255.0
    bo = b/255.0
    maxcol = max(ro, go, bo)
    mincol = min(ro, go, bo)
    deltacol = float(maxcol - mincol)
    if maxcol == mincol:
        h = 0
    elif maxcol == ro:
        h = 60 * (((go - bo) / deltacol) % 6)
    elif maxcol == go:
        h = 60 * (((bo - ro) / deltacol) + 2.0)
    elif maxcol == bo:
        h = 60 * (((ro - go) / deltacol) + 4.0)
    if h < 0:
        h += 360
    if maxcol == 0:
        s = 0
    else:
        s = deltacol/maxcol
    v = maxcol
    return h, s, v


# HSV_TO_RGB:
# takes three integer values representing the hsv color values of a picture
# performs a conversion to rgb color space
# returns a tuplet of 3 integers
def hsv_to_rgb(h, s, v):
    c = v*s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c
    rgb = (0, 0, 0)
    if h >= 0 and h < 60:
        rgb = (c, x, 0)
    elif h >= 60 and h < 120:
        rgb = (x, c, 0)
    elif h >= 120 and h < 180:
        rgb = (0, c, x)
    elif h >= 180 and h < 240:
        rgb = (0, x, c)
    elif h >= 240 and h < 300:
        rgb = (x, 0, c)
    elif h >= 300 and h < 360:
        rgb = (c, 0, x)
    new_r = int(round((rgb[0]+m)*255))
    new_g = int(round((rgb[1]+m)*255))
    new_b = int(round((rgb[2]+m)*255))
    return new_r, new_g, new_b


# USAGE: a utility function to handle printing and quitting
def usage():
    print("Usage: ./Python hueshift.py [shift number] (optional)[filename]")
    sys.exit(0)


# HUE_SHIFT:
# handles commandline arguments and opens an image using picture2.py
# funnels each pixel to the color space functions defined above
# performs the hue shift, and displays the modified image
def hue_shift(argv):
    if ((len(argv) < 2) or (len(argv) > 3)):
        usage()
    img_file = "cat.bmp" if len(argv) == 2 else argv[1]
    shift_num = 0
    # try block 1: get int from args
    try:
        shift_num = int(argv[1])
    except ValueError:
        print("Error: the shift number was not a valid number")
        usage()
    except TypeError:
        print("Error: the shift number was not a number")
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
    new_pic = picture2.Picture(width, height)

    for i in range(width):
        for j in range(height):
            r, g, b = pic.getPixelColor(i, j)
            h, s, v = rgb_to_hsv(r, g, b)
            h += (shift_num % 360)
            if h > 359:
                h -= 360
            if h < 0:
                h += 360
            r, g, b = hsv_to_rgb(h, s, v)
            new_pic.setPixelColor(i, j, int(r), int(g), int(b))
    new_pic.display()
    input("Press any key to exit: ")


if __name__ == "__main__":
    hue_shift(sys.argv)

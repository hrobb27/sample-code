"""
Created By Hamish Robb in March 2019
Last Updated 5/25/2021
---------------------------------
||**||**|| dottify.py ||**||**||
---------------------------------
Args: (int) diameter, (string) file_name
---------------------------------
Desc: this program takes an image and represents it as dot(s) of
user-specified diameter. the number of dots is however many dots
there are that can be evenly placed into the smallest dimension
of the image, squared. the output is (+/- the remainder) a square
of that smallest dimension.
"""
import sys
import picture2


# USAGE: a utility function to handle printing and quitting
def usage():
    print("Usage: Python ./dottify.py [diameter] (optional)[file name]")
    sys.exit(0)


# DOTTIFY:
# handles commandline arguments and opens an image using picture2.py
# partitions the image into dots by sampling and re-drawing with spheres
# displays the image
def dottify(argv):
    if (len(argv) < 2 or len(argv) > 3):
        print("Error: incorrect number of arguments")
        usage()
    diameter = 0
    img_file = "cat.bmp" if len(argv) == 2 else argv[1]
    # try block 1: get int from args
    try:
        diameter = int(sys.argv[1])
    except ValueError:
        print("Error: the diameter was not a valid number")
        usage()
    except TypeError:
        print("Error: the diameter was not a number")
        usage()
    except:
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
    if diameter > width or diameter > height:
        print("Error: Can't fit a dot of size ", diameter)
        usage()
    min_dimension = min(width, height)
    chunk_num = min_dimension // diameter
    # rather than going by width (only possible in fp pixel world)
    # this accounts for the possible remainder from division
    new_dimension = chunk_num * (min_dimension // chunk_num)
    newpic = picture2.Picture(new_dimension, new_dimension)
    for i in range(0, min_dimension, chunk_num):
        for j in range(0, min_dimension, chunk_num):
            r, g, b = pic.getPixelColor(i, j)
            newpic.setFillColor(r, g, b)
            newpic.drawCircleFill(i+chunk_num//2, j+chunk_num//2, chunk_num)
    newpic.display()
    input("Press any key to exit: ")


if __name__ == "__main__":
    dottify(sys.argv)

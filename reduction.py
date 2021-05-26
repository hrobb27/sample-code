"""
Created By Hamish Robb in March 2019
Last Updated 5/25/2021
---------------------------------
||**||**|| reduction.py ||**||**||
---------------------------------
Args: (int) diameter, (string) file_name
---------------------------------
Desc: this program takes a user-specified factor to divide 
a user provided (or default) image into proportional rectangular
blocks. each block has the average of the rgb of each divided
block in space. 
"""
import sys
import picture2

# USAGE: a utility function to handle printing and quitting
def usage():
    print("Usage: Python ./reduction.py [factor] (optional)[file name]")
    sys.exit(0)


# REDUCTION:  
# parses the args and opens the file
def reduction(argv):
    if (len(argv) < 2 or len(argv) > 3):
        print("Error: incorrect number of arguments")
        usage()
    factor = 0
    try:
        factor = int(argv[1])
    except ValueError:
        print("Error: the diameter was not a valid number")
        usage()
    except TypeError:
        print("Error: the diameter was not a number")
        usage()
    except:
        usage()
    img_file = "cat.bmp" if len(argv) == 2 else argv[1]
    # try block 2: open file from args or default pic
    pic = None
    try:
        pic = picture2.Picture(img_file)
    except:
        print("Error: unable to open the specified file")
        usage()
    width = pic.getWidth()
    height = pic.getHeight()
    if factor > width or factor > height:
        print("Error: the given number of grids is too large")
        usage()
    grid_width = (width // factor)
    grid_height = (height // factor)
    new_width = grid_width*factor
    new_height = grid_height*factor
    newpic = picture2.Picture(width, height)
    print(width, " | ", grid_width*factor)
    gridsize = grid_width*grid_height
    for i in range(0, width, grid_width):
        for j in range(0, height, grid_height):
            avgred = 0
            avggreen = 0
            avgblue = 0
            offsetw = i + grid_width
            offseth = j + grid_height
            if (offsetw) > width:
                offsetw = width-1
            if offseth > height:
                offseth = height-1
            for m in range(i, offsetw):
                for n in range(j, offseth):
                    avgred += pic.getPixelRed(m, n)
                    avggreen += pic.getPixelGreen(m, n)
                    avgblue += pic.getPixelBlue(m, n)
            avgred = avgred // gridsize
            avggreen = avggreen // gridsize
            avgblue = avgblue // gridsize
            for p in range(i, offsetw):
                for q in range(j, offseth):
                    newpic.setPixelColor(p, q, avgred, avggreen, avgblue)
    newpic.display()
    input("Press any key to exit: ")


if __name__ == "__main__":
    reduction(sys.argv)
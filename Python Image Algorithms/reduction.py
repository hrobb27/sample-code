#average_col.py
#for a user given grid, averages the colors of a picture
import sys
import picture2
gridnum = 0
try:
    gridnum = int(sys.argv[1])
except:
    print("Error: no grid size specified by user")
    exit()
pic = picture2.Picture("cat.bmp")

width = pic.getWidth();
height = pic.getHeight();
newpic = picture2.Picture(width, height)


if gridnum > width or gridnum > height:
    print("Error: the given number of grids is too large")
    exit()

gridwidth = (width // gridnum)
gridheight = (height // gridnum)
gridsize = gridwidth*gridheight
for i in range(0, width, gridwidth):
    for j in range(0, height, gridheight):
        avgred = 0;
        avggreen = 0;
        avgblue = 0;
        offsetw = i + gridwidth
        offseth = j + gridheight
        if (offsetw) > width:
            offsetw = width
        if offseth > height:
            offseth = height
        for m in range(i, offsetw):
            for n in range(j, offseth):
                avgred += pic.getPixelRed(m, n)
                avggreen += pic.getPixelGreen(m, n)
                avgblue += pic.getPixelBlue(m, n)
        avgred = avgred // gridsize;
        avggreen = avggreen // gridsize;
        avgblue = avgblue // gridsize;
        for p in range(i, offsetw):
            for q in range(j, offseth):
                newpic.setPixelColor(p, q, avgred, avggreen, avgblue)
newpic.display()
input("Press any key to close: ")
    
import sys
import picture2
chunknum = 0
try:
    chunknum = int(sys.argv[1])
except:
    print("Error: no grid size specified by user")
    exit()
pic = picture2.Picture("cat.bmp")

width = pic.getWidth();
height = pic.getHeight();
newpic = picture2.Picture(width, height)


if chunknum > width or chunknum > height:
    print("Error: the given number of grids is too large")
    exit()

wchunks = width//chunknum
hchunks = height//chunknum
for i in range(0, width, wchunks):
    for j in range(0, height, hchunks):
        r, g, b = pic.getPixelColor(i, j)
        newpic.setFillColor(r, g, b)
        newpic.drawCircleFill(i+wchunks/2, j+wchunks/2, wchunks/2)
newpic.display()
input("Press any key to close: ")
    
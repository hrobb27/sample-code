import sys
import picture2
chunknum = 0
try:
    chunknum = int(sys.argv[1])
except:
    print("Usage: python3 dottify.py [dot width]")
    exit()
pic = picture2.Picture("cat.bmp")

width = pic.getWidth();
height = pic.getHeight();
newpic = picture2.Picture(width, height)


if chunknum > width or chunknum > height:
    print("Can't fit a dot of size ", chunknum)
    exit()

wchunks = width//chunknum
hchunks = height//chunknum
for i in range(0, width, wchunks):
    for j in range(0, height, hchunks):
        r, g, b = pic.getPixelColor(i, j)
        newpic.setFillColor(r, g, b)
        newpic.drawCircleFill(i+wchunks/2, j+hchunks/2, wchunks)
newpic.display()
input("Press any key to close: ")
    

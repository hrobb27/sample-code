import sys
import math
import picture2
offsetnum = 0
try:
    offsetnum = int(sys.argv[1])
    wlength = int(sys.argv[2])
except:
    print("Usage: python3 wavy.py [offset] [length of wave]")
    exit()
pic = picture2.Picture("cat.bmp")

width = pic.getWidth();
height = pic.getHeight();
newpic = picture2.Picture(width, height)


offsetnum %= height

for i in range(0, width):
    for j in range(0, height):
        r, g, b = pic.getPixelColor(i, j)
        offset = int(round(offsetnum*math.sin(1/wlength*i)))
        j += offset
        if j >= height:
            j -= height
        if j < 0:
            j += height
        newpic.setPixelColor(i, j, r, g, b)
        
newpic.display()
input("Press any key to close: ")
    

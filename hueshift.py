import sys
import picture2
import colorsys
try:
    shiftnum = int(sys.argv[1])
except:
    print("Error: no hue shift was specified")
    exit()
pic = picture2.Picture("cat.bmp")

width = pic.getWidth();
height = pic.getHeight();
newpic = picture2.Picture(width, height)

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
        h = 60 * (((go - bo)/deltacol)%6)
    elif maxcol == go:
        h = 60 * (((bo-ro)/deltacol) + 2.0)
    elif maxcol == bo:
        h = 60 * (((ro-go)/deltacol) + 4.0)
    
    if h < 0:
        h += 360
    if maxcol == 0:
        s = 0
    else:
        s = deltacol/maxcol
    v = maxcol
    return h, s, v
def hsv_to_rgb(h, s, v):
    c = v*s
    x = c * (1 - abs((h/60)%2 - 1))
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
    rgb = (int(round((rgb[0]+m)*255)), int(round((rgb[1]+m)*255)), int(round((rgb[2]+m)*255)))
    return rgb
for i in range(width):
    for j in range(height):
        r, g, b = pic.getPixelColor(i, j)
        h, s, v = rgb_to_hsv(r, g, b)
        h += (shiftnum%360)
        if h > 359:
            h -= 360
        if h < 0:
            h += 360
        r, g, b = hsv_to_rgb(h, s, v)
        newpic.setPixelColor(i, j, int(r), int(g), int(b))
newpic.display()
input(":")
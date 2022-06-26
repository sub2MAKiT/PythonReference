from PIL import Image
import math
im = Image.open(input("file: "))
source = im.split()

R,G,B = 0,1,2

finalRed = 0
finalGreen = 0
finalBlue = 0

for height in range(im.size[0]):
    for width in range(im.size[1]):
        finalRed += source[R].getpixel((height, width))
        finalGreen += source[G].getpixel((height, width))
        finalBlue += source[B].getpixel((height, width))


print("R: {} G: {} B: {}".format(finalRed,finalGreen,finalBlue))
if (finalRed > finalGreen)&(finalRed > finalBlue):
    print("red")
elif (finalGreen > finalRed)&(finalGreen > finalBlue):
    print("green")
elif (finalBlue > finalGreen)&(finalRed < finalBlue):
    print("blue")

# R, G, B = 0, 1, 2

# # select regions where red is less than 100
# mask = source[R].point(lambda i: i < 100 and 255)

# # process the green band
# out = source[G].point(lambda i: math.floor(i * 0.7))

# # paste the processed band back, but only where red was < 100
# source[G].paste(out, None, mask)

# # build a new multiband image
# im = Image.merge(im.mode, source)
# im.save("final.png", "png", optimize=True, quality=80)

# im = Image.merge("RGB", (a,g,b))
# im.save("red.jpeg", "JPEG", optimize=True, quality=80)
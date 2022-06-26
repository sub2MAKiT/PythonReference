from PIL import Image
import math
im = Image.open("base.png")
pixels = im.load()

for j in range(4096):
    i = 4096-j
    y = (i-2048)*(i-2048)+(i-2048)*2+10
    if (y < 2048)&(y > -2048):
        pixels[y+2048,i] = (50, 0 ,0)
out = im.transpose(Image.Transpose.ROTATE_90)
out.save("test.png", "png", optimize=True, quality=80)
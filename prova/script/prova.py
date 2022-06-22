from PIL import Image

img = Image.open('map1.pgm')
pixval = img.load()
columnsize, rowsize = img.size 
img1 = Image.open('map.pgm')
for i in range(rowsize):
    for j in range(columnsize):
        img1.putpixel((j, i), 250)
img1.save("share1.pgm")



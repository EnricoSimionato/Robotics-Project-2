#!/usr/local/bin/python3
import numpy as np
from PIL import Image

# Load the image from disk
im = Image.open("map.pgm")

# Convert image to numpy array
na = np.array(im)

# Make entire image grey (128)
#na[:,:] = 128

# Make pixel 1,1 white (255)
#na[1,1] = 255

# Make rows 20-30 white (255)
#na[700:720,650:700] = 125

# Make columns 80-100 black (0)
#na[:,80:100] = 0

# Convert numpy array back to image and save

f = open('pose.txt', 'r')
for x in np.arange(0, 51, 1):
	for y in np.arange(0,10,1):
		f.readline()
	x_str = f.readline()[9:]
	x_value = int(float(x_str) * 20)
	y_str = f.readline()[9:]
	y_value = int(float(y_str) * 20)
	na[800+x_value:801+x_value,800+y_value:801+y_value] = 0
	for z in np.arange(0,7,1):
		f.readline()
	
f.close

Image.fromarray(na).save("result.png")

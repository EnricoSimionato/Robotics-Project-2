#!/usr/local/bin/python3

import cv2
import numpy as np
from PIL import Image

# Load the image from disk
img = cv2.imread("map1.pgm")
img_copy = img.copy()
rows,cols = img_copy.shape[:2] 
M = cv2.getRotationMatrix2D((cols/2,rows/2),265,1) 
img_copy = cv2.warpAffine(img_copy,M,(cols,rows)) 

f = open('pose.txt', 'r')
for y in np.arange(0,10,1):
	f.readline()
x_str = f.readline()[9:]
x_value_prec = int(float(x_str) * 20)
y_str = f.readline()[9:]
y_value_prec = int(float(y_str) * 20)
img_copy[800+x_value_prec][800+y_value_prec] = np.array([255,0,0])
for z in np.arange(0,7,1):
	f.readline()

for x in np.arange(0, 196, 1):
	for y in np.arange(0,10,1):
		f.readline()
	x_str = f.readline()[9:]
	x_value = int(float(x_str) * 20)
	y_str = f.readline()[9:]
	y_value = int(float(y_str) * 20)
	img_copy[800+x_value][800+y_value] = np.array([255,0,0])
	for z in np.arange(0,7,1):
		f.readline()
	while (x_value_prec != x_value or y_value_prec != y_value):
		if (x_value_prec < x_value):
			img_copy[800+x_value_prec][800+y_value_prec] = np.array([255,0,0])
			x_value_prec += 1
		if (x_value_prec > x_value):
			img_copy[800+x_value_prec][800+y_value_prec] = np.array([255,0,0])
			x_value_prec -= 1
		if (y_value_prec < y_value):
			img_copy[800+x_value_prec][800+y_value_prec] = np.array([255,0,0])
			y_value_prec += 1
		if (y_value_prec > y_value):
			img_copy[800+x_value_prec][800+y_value_prec] = np.array([255,0,0])
			y_value_prec -= 1


f.close
cv2.imwrite("map_with_trajectory.png", img_copy[350:1200, 450:1200])



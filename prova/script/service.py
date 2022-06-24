#!/usr/bin/env python
import cv2
import numpy as np
from PIL import Image
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from std_srvs.srv import Empty

x_value_prec = 0
y_value_prec = 0
isFirstTime = True
img = cv2.imread("map1.pgm")
img_copy = img.copy()
rows,cols = img_copy.shape[:2] 
M = cv2.getRotationMatrix2D((cols/2,rows/2),265,1) 
img_copy = cv2.warpAffine(img_copy,M,(cols,rows))

def callback(data):
	global x_value_prec
	global y_value_prec
	global isFirstTime
	global img_copy
	if isFirstTime:
		x_value_prec = int(data.pose.pose.position.x * 20)
		y_value_prec = int(data.pose.pose.position.y * 20)
		isFirstTime = False 
		img_copy[800+x_value_prec][800+y_value_prec] = np.array([255,0,0])
   	else:
		x_value = int(data.pose.pose.position.x * 20)
		y_value = int(data.pose.pose.position.y * 20)
		img_copy[800+x_value][800+y_value] = np.array([255,0,0])
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


def draw_trajectory(req):
	global img_copy
	print("Drawing trajectory")
	cv2.imwrite("map_with_trajectory.png", img_copy[350:1200, 450:1200])
	return Empty

def listener():

	    rospy.init_node('trajectory_drawer', anonymous=True)
	
            rospy.Subscriber("amcl_pose", PoseWithCovarianceStamped, callback)
      
     	    s = rospy.Service('draw_trajectory', Empty, draw_trajectory)
	    rospy.spin()

if __name__ == '__main__':
  	    listener()

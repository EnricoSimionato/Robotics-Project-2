#!/usr/bin/env python

import rospy
from std_srvs.srv import Empty
    
  
def get_trajectory():
	rospy.wait_for_service('draw_trajectory')
	try:
		draw_trajectory = rospy.ServiceProxy('draw_trajectory', Empty)
		draw_trajectory()
		print("Drawing trajectory")
	except rospy.ServiceException as e:
		print("Error: %s" %e)
   
   
if __name__ == "__main__":
	get_trajectory()


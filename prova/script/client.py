#!/usr/bin/env python

import rospy
from std_srvs.srv import Empty
    
  
def get_trajectory():
	rospy.wait_for_service('draw_trajectory')
	draw_trajectory = rospy.ServiceProxy('draw_trajectory', Empty)
	resp1 = draw_trajectory()
	print("Drawing trajectory")
   
   
if __name__ == "__main__":
	get_trajectory()


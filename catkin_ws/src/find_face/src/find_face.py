#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from math import radians
from time import sleep
pup = rospy.Publisher('/keyop_vel_smoother/raw_cmd_vel', Twist, queue_size=1)

def callback(data):
	x=int(data.data)
	rospy.loginfo("string to int %d",x)
	#movement here
        r = rospy.Rate(50);
        
	#let's turn at 45 deg/s
        turn_cmd = Twist()
        turn_cmd.linear.x = 0
	
	#if x is small which face is at the left keep turn left until (x center 250) fuzzy logic 
	#range 240-260
	
	if 220 <= x <= 280 :
		rospy.loginfo("STOP TURNING")
		r.sleep()
	elif x < 220 :
		#turn left 
		rospy.loginfo("Turning left")
        	turn_cmd.angular.z = radians(10);
		pup.publish(turn_cmd)
		r.sleep()
	elif x>280 :
		#turn right
		rospy.loginfo("Turning right")
		turn_cmd.angular.z = radians(-10);
		pup.publish(turn_cmd)
		r.sleep()

		

	#two keep going back and forth. Go forward for 2 seconds (10 x 5 HZ) then turn for 3 second
'''        while not rospy.is_shutdown():
		for x in range(0,6):
			rospy.loginfo("Turning")
   			self.cmd_vel.publish(turn_cmd)
         		r.sleep()
'''
	
	
def find_face():
	rospy.init_node('find_face',anonymous=True)
	rospy.Subscriber("face_rec/pos_x",String, callback)
	rospy.spin()

if __name__ == '__main__':
	try:
		find_face()

	except:
		rospy.loginfo("node terminated.")



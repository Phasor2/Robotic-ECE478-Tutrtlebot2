#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Int32
from geometry_msgs.msg import Twist
from math import radians
from time import sleep
pup = rospy.Publisher('/keyop_vel_smoother/raw_cmd_vel', Twist, queue_size=1)
arm = rospy.Publisher('arm_act',Int32, queue_size=1)

def callback(data):
	x=int(data.data)
	rospy.loginfo("string to int %d",x)
	#movement here
        r = rospy.Rate(30);
        
	#initialize arm_value 1 activate, 0 deactivate
	arm_value=0
	#let's turn at 45 deg/s
        turn_cmd = Twist()
        turn_cmd.linear.x = 0
	
	#if x is small which face is at the left keep turn left until (x center 250) fuzzy logic 
	#range 240-260
	
	if 220 <= x <= 280 :
		rospy.loginfo("STOP TURNING")
		
		#activate arm
		arm_value = 1
		arm.publish(arm_value)
		r.sleep()
	elif x < 220 :
		#turn left 
		rospy.loginfo("Turning left")
        	turn_cmd.angular.z = radians(10);
		pup.publish(turn_cmd)
	
		#deactivate arm
		arm_value = 0
		arm.publish(arm_value)

		r.sleep()
	elif x>280 :
		#turn right
		rospy.loginfo("Turning right")
		turn_cmd.angular.z = radians(-10);
		pup.publish(turn_cmd)
		
		#deactivate arm
		arm_value = 0
		arm.publish(arm_value)

		r.sleep()
		
	
	
def find_face():
	rospy.init_node('find_face',anonymous=True)
	rospy.Subscriber("face_rec/pos_x",String, callback)
	rospy.spin()

if __name__ == '__main__':
	try:
		find_face()

	except:
		rospy.loginfo("node terminated.")



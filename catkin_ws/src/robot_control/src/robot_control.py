#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from math import radians
from std_msgs.msg import Int32
from time import sleep
pub = rospy.Publisher('/keyop_vel_smoother/raw_cmd_vel', Twist, queue_size=1)

def callback(data):
	rospy.loginfo("Command numer: %d", data.data)
	x=data.data
	r = rospy.Rate(5);
	go_cmd =Twist()
	turn_cmd =Twist()
	if x==1:
		rospy.loginfo("GO STRAIGHT")
		go_cmd.linear.x=0.3
		pub.publish(go_cmd)
		r.sleep()
    
	elif x==2:
		rospy.loginfo("TURN LEFT")
		turn_cmd.linear.x=0
		turn_cmd.angular.z=radians(180);
		pub.publish(turn_cmd)
		r.sleep()
	elif x==3:
		rospy.loginfo("TURN RIGHT")
		turn_cmd.linear.x=0
		turn_cmd.angular.z=radians(-180);
		pub.publish(turn_cmd)
		r.sleep()
	#draw a square
	elif x==4:
		y = 0
		while y !=1 :
			for y in range(0,15):
				rospy.loginfo("GO STRAIGHT")
				go_cmd.linear.x=0.2
				pub.publish(go_cmd)
				r.sleep()
			sleep(1)
			for y in range (0,11):
				rospy.loginfo("TURNING")
				turn_cmd.linear.x=0
				turn_cmd.angular.z=radians(55.65)
				pub.publish(turn_cmd)
				r.sleep()
			sleep(1)
	#draw a triangle
	elif x==5:
		y = 0
		while y !=1 :
			for y in range(0,10):
				rospy.loginfo("GO STRAIGHT")
				go_cmd.linear.x=0.3
				go_cmd.angular.z = 0
				pub.publish(go_cmd)
				r.sleep()
			sleep(1)
			for y in range (0,15):
				rospy.loginfo("TURNING")
				turn_cmd.linear.x=0
				turn_cmd.angular.z=radians(45)
				pub.publish(turn_cmd)
				r.sleep()
			sleep(1)

	#back and fort
	elif x==6:
		y = 0
		while y !=1 :
			for y in range(0,15):
				rospy.loginfo("GO STRAIGHT")
				go_cmd.linear.x=0.3
				go_cmd.angular.z = 0
				pub.publish(go_cmd)
				r.sleep()
			sleep(1)

		#turn 180
			for y in range (0,14):
				rospy.loginfo("TURNING")
				turn_cmd.linear.x=0
				turn_cmd.angular.z=radians(83)
				pub.publish(turn_cmd)
				r.sleep()
			sleep(1)

	#draw a circle Counterclockwise
	elif x==7:
		y = 0
		while y !=1 :
			rospy.loginfo("GO circle counter clockwise")
			go_cmd.linear.x=0.3
			go_cmd.angular.z = radians(90)
			pub.publish(go_cmd)
			r.sleep()
	#draw a circle Clockwise
	elif x==8:
		y = 0
		while y !=1 :
			rospy.loginfo("GO circle counter clockwise")
			go_cmd.linear.x=0.3
			go_cmd.angular.z = radians(-90)
			pub.publish(go_cmd)
			r.sleep()

							
											


def robot_control():

	rospy.init_node('robot_control', anonymous=True)
	#SUBSRIBE TO TOPIC
	rospy.Subscriber("motion_num", Int32, callback)

	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()

if __name__ == '__main__':
	try:
		robot_control()
	except:
		rospy.loginfo("node terminated.")

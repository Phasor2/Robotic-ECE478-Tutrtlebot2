#!/usr/bin/env python


import rospy
from geometry_msgs.msg import Twist
from math import radians


class Straight():
	def __init__(self):
        	# initiliaze
       		rospy.init_node('test', anonymous=False)

        	# What to do you ctrl + c    
        	rospy.on_shutdown(self.shutdown)

        	self.cmd_vel = rospy.Publisher('/keyop_vel_smoother/raw_cmd_vel', Twist, queue_size=10)

       		# 5 HZ
        	r = rospy.Rate(5);

        	# create two different Twist() variables.  One for moving forward.  One for turning 45 degrees.

        	# let's go forward at 0.2 m/s
        	move_cmd = Twist()
        	move_cmd.linear.x = 0.2
		move_cmd.angular.z = 0.0

        	# by default angular.z is 0 so setting this isn't required

        	#let's turn at 45 deg/s left
        	turn_cmd = Twist()
        	turn_cmd.linear.x = 0
        	turn_cmd.angular.z = radians(-10); #180 deg/s in radians/s


		#two keep going back and forth. Go forward for 2 seconds (10 x 5 HZ) then turn for 3 second
        	count = 0
        	while not rospy.is_shutdown():
                #		r.sleep()
            		# turn 180 degrees
			for x in range(0,6):
            			rospy.loginfo("Turning")
            			self.cmd_vel.publish(turn_cmd)
            			r.sleep()

	def shutdown(self):
        	# stop turtlebot
		rospy.loginfo("Stop moving")
		self.cmd_vel.publish(Twist())
		rospy.sleep(1)

if __name__ == '__main__':
    try:
        Straight()
    except:
        rospy.loginfo("node terminated.")



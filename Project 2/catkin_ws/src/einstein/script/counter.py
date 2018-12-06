#!/usr/bin/env python

'''
increments lines for play
'''


import rospy

from std_msgs.msg import Int32


def incrementCallback(data):
	increment = data.data
	increment = increment + 1
	line_num.publish(increment)
	return

rospy.init_node("Counter")
line_num = rospy.Publisher('/lines', Int32, queue_size=1)
rospy.Subscriber("/increment",Int32,incrementCallback)

rospy.spin()


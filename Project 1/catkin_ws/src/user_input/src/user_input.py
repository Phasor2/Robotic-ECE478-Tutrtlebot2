#!/usr/bin/env python
# BEGIN ALL
import rospy
import sys
from std_msgs.msg import Int32
from sensor_msgs.msg import Image
import argparse, textwrap




def User_input():
	# DECLARE TOPIC
	pub = rospy.Publisher('motion_num', Int32, queue_size=10)
	rospy.init_node('user_input', anonymous=True)

	parser = argparse.ArgumentParser(description='Robot_controller',usage='use "roslaunch user_input user_input.launch -num" for more information -help', formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument("num", type=int, default=1,help=textwrap.dedent('''\
1 = Go forward
2 = Spin Left
3 = Spin Right
4 = Draw a Square
5 = Draw a Triangle 
6 = Go back and Fort
7 = Circle Counterclockwise
8 = Circle Clockwise
'''))
	args = parser.parse_args()

	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
		pub.publish(args.num)
		rate.sleep()

if __name__ == '__main__':
    try:
        User_input()
    except rospy.ROSInterruptException:
        pass


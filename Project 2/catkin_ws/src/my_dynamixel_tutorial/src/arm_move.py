#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Int32, Float64
from geometry_msgs.msg import Twist
from math import radians
from time import sleep
arm1 = rospy.Publisher('/tilt_controller1/command', Float64, queue_size=1)
arm2 = rospy.Publisher('/tilt_controller2/command', Float64, queue_size=1)
arm3 = rospy.Publisher('/tilt_controller3/command', Float64, queue_size=1)
arm4 = rospy.Publisher('/tilt_controller4/command', Float64, queue_size=1)
arm5 = rospy.Publisher('/tilt_controller5/command', Float64, queue_size=1)
arm6 = rospy.Publisher('/tilt_controller6/command', Float64, queue_size=1)
arm7 = rospy.Publisher('/tilt_controller7/command', Float64, queue_size=1)
arm8 = rospy.Publisher('/tilt_controller8/command', Float64, queue_size=1)
arm9 = rospy.Publisher('/tilt_controller9/command', Float64, queue_size=1)
arm10 = rospy.Publisher('/tilt_controller10/command', Float64, queue_size=1)



def callback(data):
	arm_val=data.data
	rospy.loginfo("activate is %d",arm_val)
	#movement here
        r = rospy.Rate(0.8);
        
	#initialize arm_value 1 activate, 0 deactivate

	if arm_val==0 :
		rospy.loginfo("Normal mode")
		
		#Normal mode
		arm1_pos = -1
		arm2_pos = -0.5
		arm3_pos = 0
		arm4_pos = 0
		arm5_pos = 0.5
		arm6_pos = 0.5
		arm7_pos = 1.5
		arm8_pos = -1
		arm9_pos = 0
		arm10_pos = 0
	
		arm1.publish(arm1_pos)
		arm2.publish(arm2_pos)
		arm3.publish(arm3_pos)
		arm4.publish(arm4_pos)
		arm5.publish(arm5_pos)
		arm6.publish(arm6_pos)
		arm7.publish(arm7_pos)
		arm8.publish(arm8_pos)
		arm9.publish(arm9_pos)
		arm10.publish(arm10_pos)

	elif arm_val==1 :
		rospy.loginfo("waving")
		arm1_pos = 1.5
		arm5_pos = 0
		arm6_pos = 1
		arm7_pos = -1	
		arm10_pos = 1


		arm1.publish(arm1_pos)
		arm5.publish(arm5_pos)
		arm6.publish(arm6_pos)
		arm7.publish(arm7_pos)
		rospy.loginfo("activate is %d",arm_val)
		for i in range (1,3):	
			#waving here
			rospy.loginfo("waving 1")
			arm2_pos = 0.5		#motion 0.5 -> -0.5
			arm2.publish(arm2_pos)
			arm8_pos = -0.5		#motion -0.5 -> -1	
			arm8.publish(arm8_pos)
			r.sleep()
			rospy.loginfo("waving 2")
			arm2_pos = -0.5
			arm2.publish(arm2_pos)
			arm8_pos = -1		
			arm8.publish(arm8_pos)
			arm10.publish(arm10_pos)
			arm_val=0
			rospy.loginfo("arm_val: %d",arm_val)
			r.sleep()
				
	
	
rospy.init_node('arm_move',anonymous=True)
rospy.Subscriber("/arm_act",Int32, callback)
rospy.spin()




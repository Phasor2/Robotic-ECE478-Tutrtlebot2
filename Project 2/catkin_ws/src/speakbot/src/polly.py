#!/usr/bin/env python
import pdb
import rospy
import boto3
import os
from playsound import playsound
from subprocess import Popen
from std_msgs.msg import String,Int32

arm = rospy.Publisher('/arm_act', Int32, queue_size=1)


polly_client = boto3.Session(aws_access_key_id='###################',aws_secret_access_key='###################################',region_name='us-west-2').client('polly')

def callback(data):	
	response = polly_client.synthesize_speech(VoiceId='Matthew',OutputFormat='mp3',Text = data.data)
	file = open('/home/myturtlebot/catkin_ws/speech.mp3', 'w')
	file.write(response['AudioStream'].read())
	file.close()
	playsound("/home/myturtlebot/catkin_ws/speech.mp3")
	
	r = rospy.Rate(0.2);
	value=1
	arm.publish(value)
	r.sleep()
	value=0
	arm.publish(value)
	r.sleep()






rospy.init_node("speakingbot")
rospy.Subscriber("/response",String,callback)
rospy.spin()


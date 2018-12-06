#!/usr/bin/env python
import pdb
#debug
#pdb.set_trace()
import rospy
from std_msgs.msg import String
import speech_recognition as sr
import argparse
import uuid
import os
import dialogflow_v2 as dialogflow
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/home/myturtlebot/Downloads/Robotic-5595bb2b581d.json'
project_id = 'robotic-223705'
session_id = str(uuid.uuid4())
language_code='en-US'
BOTNAME="John"
r = sr.Recognizer()
m = sr.Microphone()

pub = rospy.Publisher('/response', String, queue_size=10)


def callback(res):
	#Start to publish the topic /response
	res = str(res)
	rospy.loginfo(res)
	pub.publish(res)

def detect_intent_texts(texts):
	global project_id,session_id,language_code 
	
	#Dialogflow Google process
	session_client = dialogflow.SessionsClient()
	session = session_client.session_path(project_id, session_id)
	for text in texts:
		text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
        	query_input = dialogflow.types.QueryInput(text=text_input)
        	response = session_client.detect_intent(session=session, query_input=query_input)
        	print('{}\n'.format(response.query_result.fulfillment_text))
		callback(response.query_result.fulfillment_text)	
	
rospy.init_node("talkingbot")
#prepare the microphone
try:
	print("A moment of silence, please...")
	while True:
	        with m as source: r.adjust_for_ambient_noise(source)
	        print("Set minimum energy threshold to {}".format(r.energy_threshold))
	        print("Say something!")
	        with m as source: audio = r.listen(source)
	        print("Got it! Now to recognize it...")
		value="r"
		try:
			# recognize speech using Google Speech Recognition
			value = r.recognize_google(audio)
			print(value)
		except sr.UnknownValueError:
			pass
		except sr.RequestError as e:
			print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
		pos=0
		pos=value.find(BOTNAME)
		if pos != -1:
			#filter the bot name
			value=value.replace(BOTNAME,'')
			#remove the white space
			value = value[:pos] + value[(pos+1):]
			if len(value)>3:
				#unicode to string
				texts= str(value)
				#string to list
				texts=[texts]
				print(texts)
				detect_intent_texts(texts)
except rospy.ROSInterruptException:
	pass
except KeyboardInterrupt:
	pass

rospy.spin()

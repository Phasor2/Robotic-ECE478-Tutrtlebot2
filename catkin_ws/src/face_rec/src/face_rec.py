#!/usr/bin/env python
# BEGIN ALL
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
import cv2, cv_bridge
from time import sleep

face_cascade = cv2.CascadeClassifier('/home/phong/facial_rec/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/phong/facial_rec/haarcascade_eye.xml')

class face_rec:


	def __init__(self):
		self.bridge = cv_bridge.CvBridge()
		self.image_sub = rospy.Subscriber('camera/rgb/image_raw',Image, self.image_callback)

	def image_callback(self, msg):
		rate = rospy.Rate(10) # 10hz
		image = self.bridge.imgmsg_to_cv2(msg,"bgr8")
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
		for (x,y,w,h) in faces:
			cv2.rectangle(image, (x,y), (x+w, y+h),(255,0,0), 2)
			roi_gray = gray[y:y+h, x:x+w]
			roi_color = image[y:y+h, x:x+w]
			eyes =eye_cascade.detectMultiScale(roi_gray)
			rospy.loginfo("x: %d and y: %d", x, y)

			pub = rospy.Publisher('face_rec/pos_x',String, queue_size=1)
			pub.publish(str(x))
			rate.sleep()

			for (ex,ey,ew,eh) in eyes:
				cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0),2)
		cv2.imshow('afterimg',image)
		cv2.waitKey(3)


rospy.init_node('face_rec')
Face_rec = face_rec()
rospy.spin()
# END ALL


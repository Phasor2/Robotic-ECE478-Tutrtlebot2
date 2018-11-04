import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
 
class Follower:
	def __init__(self):
		self.bridge = CvBridge()
		self.image_received = False
		cv2.namedWindow("window", 1)
		
		img_topic = "/camera/rgb/image_raw"
		self.image_sub = rospy.Subscriber(img_topic,Image, self.image_callback)
		rospy.sleep(1)

	def image_callback(self, msg):
		image = self.bridge.imgmsg_to_cv2(msg,"bgr8")
		cv2.imshow("window", image)
		cv2.waitKey(3)


rospy.init_node('Follower', anonymous=False)
follower = Follower()
rospy.spin()
# END ALL

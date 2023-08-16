import rospy
from sensor_msgs.msg import Image

from cv_bridge import CvBridge, CvBridgeError
import numpy as np
import cv2

IMAGE_TOPIC = "/camera/color/image_raw"

obs_img = None

bridge = CvBridge()

def callback_obs(msg: Image):
    global obs_img
    obs_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    cv2.imshow("frame" , obs_img)
    cv2.waitKey(3)
    
    

def main():
    global obs_img
    rospy.init_node("RS_CAMERA", anonymous=False)
    
    image_curr_msg = rospy.Subscriber(
        IMAGE_TOPIC, Image, callback_obs, queue_size=1)

    print("Registered with master node. Waiting for images...")
    
    rospy.spin()
            
            
if __name__ == "__main__":
    main()
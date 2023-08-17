import rospy
import numpy as np
from sensor_msgs.msg import Image
from PIL import Image as PILImage
import cv2


 
IMAGE_TOPIC = "/locobot/camera/color/image_raw"

obs_img = None

def msg_to_pil(msg: Image) -> PILImage.Image:
    img = np.frombuffer(msg.data, dtype=np.uint8).reshape(msg.height, msg.width, -1)
    pil_image = PILImage.fromarray(img)
    return pil_image


def callback_obs(msg: Image):
    global obs_img
    obs_img = msg_to_pil(msg)
    CV_img = cv2.cvtColor(np.asarray(obs_img),cv2.COLOR_RGB2BGR) 
    cv2.imshow("ROS Image", CV_img)
    cv2.waitKey(1)  # Display the image for a short period
    
    
if __name__ == '__main__':
    
    rospy.init_node('img_process_node', anonymous=True)
    
    rospy.Subscriber(IMAGE_TOPIC, Image, callback_obs, queue_size=1)
    rospy.spin()
    
    # Close OpenCV windows
    cv2.destroyAllWindows()
    

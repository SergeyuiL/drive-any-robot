import rospy
import numpy as np
from sensor_msgs.msg import Image
from PIL import Image as PILImage


 
IMAGE_TOPIC = "/camera/color/image_raw"
obs_img = None

def msg_to_pil(msg: Image) -> PILImage.Image:
    img = np.frombuffer(msg.data, dtype=np.uint8).reshape(msg.height, msg.width, -1)
    pil_image = PILImage.fromarray(img)
    return pil_image


def callback_obs(msg: Image):
    global obs_img
    obs_img = msg_to_pil(msg)
    obs_img.show()
    print(obs_img.mode, obs_img.size, obs_img.format)
    
    
if __name__ == '__main__':
    
    rospy.init_node('img_process_node', anonymous=True)
    
    rospy.Subscriber(IMAGE_TOPIC, Image, callback_obs, queue_size=1)
    rospy.spin()
    

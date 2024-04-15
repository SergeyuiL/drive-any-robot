import rospy
import numpy as np
from sensor_msgs.msg import Image
from PIL import Image as PILImage
import cv2
import time

img_array = []

# IMAGE_TOPIC = "/locobot/camera/color/image_raw"
IMAGE_TOPIC = "/camera/color/image_raw"

FILE = "image.mp4"
# FILE = "obs.mp4"
# FILE = "run.mp4"

obs_img = None
CV_img = None

def msg_to_pil(msg: Image) -> PILImage.Image:
    img = np.frombuffer(msg.data, dtype=np.uint8).reshape(msg.height, msg.width, -1)
    pil_image = PILImage.fromarray(img)
    return pil_image


def callback_obs(msg: Image):
    global obs_img, CV_img
    obs_img = msg_to_pil(msg)
    CV_img = cv2.cvtColor(np.asarray(obs_img),cv2.COLOR_RGB2BGR) 
    

    
    
if __name__ == '__main__':
    rospy.init_node('img_process_node', anonymous=True)
    rospy.Subscriber(IMAGE_TOPIC, Image, callback_obs, queue_size=1)
    start_time = time.time()
    while not rospy.is_shutdown():
        if CV_img is not None:
            print("Get Image")
            height, width, layers = CV_img.shape
            size = (width, height)
            img_array.append(CV_img)
            CV_img = None
        if time.time() - start_time > 42.0:
            print(f"Topic {IMAGE_TOPIC} not publishing anymore. Shutting down...")
            rospy.signal_shutdown("shutdown")
    
    out = cv2.VideoWriter(FILE, cv2.VideoWriter_fourcc('M', 'P', '4', 'V'), 20, size)
    for i in range(len(img_array)):
        out.write(img_array[i])
    print("Finished")
    out.release()

# out = cv2.VideoWriter('VideoResults.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

# for i in range(len(img_array)):
#     out.write(img_array[i])
# out.release()

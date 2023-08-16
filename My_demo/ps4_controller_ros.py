#!/usr/bin/env python3

# import threading
import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist


# from interbotix_xs_modules.locobot import InterbotixLocobotXS


JOY_INPUT = "/dev/input/js0"
JOY_TOPIC = "/joy_orig"
MV_TOPIC = "/locobot/mobile_base/commands/velocity"
# MV_TOPIC = "/turtle1/cmd_vel"

JOY_THRESHOLD = 0.2

# MAX_V = 1.5 # m/s
# MAX_W = 6.6 # rad/s
MAX_V = 0.7 # m/s
MAX_W = 3.14 # rad/s

# MAX_CAMERA_TILT = 1.0
# MAX_CAMERA_PAN = 1.0

# MAX_JOY_VALUE = 32767
MAX_JOY_VALUE = 1.0

class PS4ControllerROS:
    def __init__(self):
        rospy.init_node('ps4_controller_ros_node')

        self.joy_sub = rospy.Subscriber(JOY_TOPIC, Joy, self.joy_callback)
        self.twist_pub = rospy.Publisher(MV_TOPIC, Twist, queue_size=1)

        self.twist_msg = Twist()
        
        # self.locobot = InterbotixLocobotXS(robot_model="locobot_wx250s", arm_model="mobile_wx250s", use_move_base_action=True)

    def joy_callback(self, data):
        axes = data.axes
        buttons = data.buttons

        # Map joystick axes to Twist message linear and angular components
        # L2_joy = (MAX_JOY_VALUE - axes[2]) / 2.0
        # R2_joy = (MAX_JOY_VALUE - axes[5]) / 2.0
        # diff = R2_joy - L2_joy
        # if abs(diff) > JOY_THRESHOLD :
        #     self.twist_msg.linear.x = diff * MAX_V
        # else:
        #     self.twist_msg.linear.x = 0.0
        if abs(axes[4]) > JOY_THRESHOLD:
            self.twist_msg.linear.x = axes[4] * MAX_V
        else:
            self.twist_msg.linear.x = 0.0
        if abs(axes[0]) > JOY_THRESHOLD:
            self.twist_msg.angular.z = axes[0] * MAX_W
        else:
            self.twist_msg.angular.z = 0.0
        
        

        # Publish the Twist message
        self.twist_pub.publish(self.twist_msg)
        
        # # Camera Angle 
        # camera_tilt_angle = axes[4]
        # camera_pan_angle = axes[3]
        # # Move the camera
        # self.locobot.camera.pan_tilt_move(camera_pan_angle, camera_tilt_angle)
        
if __name__ == '__main__':
    try:
        ps4_controller = PS4ControllerROS()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass


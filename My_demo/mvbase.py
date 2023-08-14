import rospy
from geometry_msgs.msg import Twist

# continue moving on the linear vel 0.5 and the angular vel 0.3 
# until the process is shut down

VEL_TOPIC = "/locobot/mobile_base/commands/velocity"
RATE = 10

def main():
    rospy.init_node("MV_CTRL", anonymous=False)
    vel_out = rospy.Publisher(VEL_TOPIC, Twist, queue_size=1)
    rate = rospy.Rate(RATE)
    
    vel_msg = Twist()
    vel_msg.linear.x = 0.5
    vel_msg.angular.z = 0.3
    while not rospy.is_shutdown():
        vel_out.publish(vel_msg)
        rate.sleep()
        
if __name__ == '__main__':
	main()
    
    
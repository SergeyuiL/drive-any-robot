from interbotix_xs_modules.locobot import InterbotixLocobotXS


def main():
    locobot = InterbotixLocobotXS(robot_model="locobot_wx250s", arm_model="mobile_wx250s", use_move_base_action=True)
    
    # arm 
    locobot.gripper.close()
    locobot.arm.go_to_sleep_pose()
    # locobot.arm.go_to_home_pose()

    # camera
    locobot.camera.pan_tilt_go_home()
    locobot.camera.pan_tilt_move(0, 0.3)
    
    # locobot.camera.pan_tilt_go_home()

if __name__=='__main__':
    main()
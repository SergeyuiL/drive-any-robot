#!/bin/bash

# Create a new tmux session
session_name="gnm_locobot_$(date +%s)"
tmux new-session -d -s $session_name

# Split the window into four panes
tmux selectp -t 0    # select the first (0) pane
tmux splitw -h -p 50 # split it into two halves
tmux selectp -t 0    # select the first (0) pane
tmux splitw -v -p 50 # split it into two halves

tmux selectp -t 2    # select the new, second (2) pane
tmux splitw -v -p 50 # split it into two halves
tmux selectp -t 0    # go back to the first pane

tmux selectp -t 3
tmux splitw -h -p 50 # split it into two halves


# Run the roslaunch command in the first pane
tmux select-pane -t 0
tmux send-keys "roslaunch gnm_locobot.launch" Enter

# Run the navigate.py script with command line args in the second pane
tmux select-pane -t 1
tmux send-keys "conda activate gnm_deployment" Enter
tmux send-keys "python navigate.py $@" Enter

# Run the teleop.py script in the third pane
tmux select-pane -t 2
tmux send-keys "conda activate gnm_deployment" Enter
tmux send-keys "python joy_teleop.py" Enter

# Run the pd_controller.py script in the fourth pane
tmux select-pane -t 3
tmux send-keys "conda activate gnm_deployment" Enter
tmux send-keys "python pd_controller.py" Enter

tmux select-pane -t 4
tmux send-keys "cd ../topomaps/bags" Enter
tmux send-keys "rosbag record /locobot/camera/color/image_raw -o run_obs.bag" # change topic if necessary




# Attach to the tmux session
tmux -2 attach-session -t $session_name

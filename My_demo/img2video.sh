#!/bin/bash

# Create a new tmux session
session_name="teleop_locobot_$(date +%s)"
tmux new-session -d -s $session_name

# Split the window into two panes
tmux selectp -t 0    # select the first (0) pane
tmux splitw -v -p 50 # split it into two halves
tmux selectp -t 0
tmux splitw -h -p 50 # split it into two halves


# Run the roslaunch command in the first pane
tmux select-pane -t 0
tmux send-keys "conda activate gnm_deployment" Enter
tmux send-keys "python img2video.py" Enter
# tmux send-keys "roslaunch interbotix_xslocobot_control xslocobot_python.launch rtabmap_args:=-d use_lidar:=false" Enter

tmux select-pane -t 1
tmux send-keys "roscore" Enter

# Run the teleop.py script in the second pane
tmux select-pane -t 2
tmux send-keys "cd .." Enter
tmux send-keys "cd deployment/topomaps/bags" Enter
tmux send-keys "rosbag play loco_obs.bag" Enter

# Attach to the tmux session
tmux -2 attach-session -t $session_name
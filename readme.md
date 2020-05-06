## instructions for getting started with the cartobot project
## First you need to start the roscore process, this can be done with the commands below
## roscore
source ~/.bashrc
cd ~/catkin_ws
source devel/setup.bash
roscore 

## Second you will to need to start gazebo for the simulation of the turtlebot3
## To do this, use the commands below
-- open a new tab
source ~/.bashrc
cd ~/catkin_ws
source devel/setup.bash
roslaunch turtlebot3_gazebo turtlebot3_world.launch

## Commands below are for execting program for controlling the turtlebot3 using keyboard
-- open a new tab
source ~/.bashrc
cd ~/catkin_ws
source devel/setup.bash
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch


## Commands below are for execting the autonomously driving of the turtlebot3 using the lidar 
-- open a new tab
source ~/.bashrc
cd ~/catkin_ws
source devel/setup.bash
roslaunch turtlebot3_gazebo turtlebot3_simulation.launch

## Commands below are for starting the 3D visualization tool of the turtlebot
--open a new tab
source ~/.bashrc
cd ~/catkin_ws
source devel/setup.bash
roslaunch turtlebot3_gazebo turtlebot3_gazebo_rviz.launch

## Commands below are for starting the sonar program (still in progress)
-- open a new tab
source ~/.bashrc
cd ~/catkin_ws
source devel/setup.bash
roslaunch turtlebot3_example turtlebot3_sonar.launch

## listen to sonar topic, to see the data of the ultrasonic sensor
-- open a new tab
source devel/setup.bash
rostopic echo /sonar 

## Using the Python file to run the launch files
-- open a new tab
```
cd catkin_ws
source ./devel/setup.bash
rosrun runtotal ArgumentLoop.py ~/catkin_ws/Map/map <time>
```



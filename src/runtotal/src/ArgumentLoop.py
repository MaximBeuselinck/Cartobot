#!/usr/bin/env python
import roslaunch
import rospy
import os
import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
path = sys.argv[1]
#We need the place where the mapping files need to be saved as argument e.g. /home/user/catkin_ws/Map/map
try:
	arguments = "-f " + path
except:
	print(" We need a path name as argument")
	sys.exit()

#Running the launchfile that will launch all the packages we need
uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
roslaunch.configure_logging(uuid)
cli_argsStart = ['./src/runtotal/launch/mainLoop.launch']
roslaunch_argsStart = cli_argsStart[1:]
roslaunch_fileStart = [(roslaunch.rlutil.resolve_launch_arguments(cli_argsStart)[0], roslaunch_argsStart)]
parentStart = roslaunch.parent.ROSLaunchParent(uuid, roslaunch_fileStart)
parentStart.start()



#settting up the main loop that will save the map every time the given seconds as argument are over
node = roslaunch.core.Node('map_server','map_saver',args= arguments)
launch = roslaunch.scriptapi.ROSLaunch()


time = int(sys.argv[2])

cmd = "convert " + path + ".pgm " + path + ".jpg" 
while(True):
	try:
		launch.start()
		process = launch.launch(node)
		#os.system("convert ./Map/map.pgm ./Map/map.jpg")
		os.system(cmd)
		rospy.sleep(time)
	except:
		print("end of program")
		sys.exit()

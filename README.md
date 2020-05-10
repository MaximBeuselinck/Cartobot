# Cartobot
This is a project for SEE Labo.

Steven Boeckx (CEO)  
Maxim Beuselinck (CCO)  
Jeroen Vastmans  
Sam Rousseeuw  
Birte De Smedt  
Emile Carron  

# Project
  * Map the surroundings
  * Pathfinding through a room/maze
  * Detect cliffs and edges
  * Upload map to a webserver
  
# How to get started:

Run the Python file with the code below:

Arguments are: 
  * path name to save the map in;
  * time on which you want te refresh the map.

```
cd catkin_ws
source ./devel/setup.bash
rosrun runtotal ArgumentLoop.py ~/catkin_ws/Map/map <time>
```

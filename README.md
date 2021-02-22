# Self-Driving Udacity Introduction to Robotics MOOC 

The repository consists of all the programs and projects which are part of Udacity Introduction to Robotics using Artificial Intelligence MOOC. 



## Problem - 1 Search Algorithm in a Grid World

This example illustrates the search algorithm in a given grid world and goal location. 

**OBJECTIVE -** Write a program that finds the shortest path that leads the robot from the start state to the goal state. 

**GIVEN -** The grid world can be a parking structure and you want to move the robot to its goal location. For simplicity, robot can move in 4 directions. Three variables i.e. x,y & g where x,y are the grid dimensions and g is the shortest distance to the goal state. Let us assume that the robot takes certain actions with certainity. 


## Problem - 2 A* Algorithm for Path Planning 


This example illustrates the search algorithm using A* in a grid world and a goal location. 

**OBJECTIVE -** Write a program that finds the shortest path that leads the robot from the start state to the goal state and overcomes the problem faced by the traditional search algorithm.

**GIVEN -** A heuristic function of same dimensions as the main grid world to find a efficient shortest path to the goal state. The heurisitc function h(x,y) <= distance to goal from x,y
Five variables i.e. x,y,f,g & h where (x,y) are the grid dimensions, h is the value from the heuristic function at given (x,y), g is the shortest distance to the goal state & f is (g+h). 
Let us assume that the robot takes certain actions with certainity.

#########################################################################################################################################

# This example illustrates the search algorithm using A* in a grid world and a goal location. 

# OBJECTIVE - Write a program that finds the shortest path that leads the robot from the start state to the goal state and overcomes the problem faced by the traditional search algorithm.

# GIVEN - 
# A heuristic function of same dimensions as the main grid world to find a efficient shortest path to the goal state. The heurisitc function h(x,y) <= distance to goal from x,y
# Five variables i.e. x,y,f,g & h where (x,y) are the grid dimensions, h is the value from the heuristic function at given (x,y), g is the shortest distance to the goal state & f is (g+h). 
# Let us assume that the robot takes certain actions with certainity.

###########################################################################################################################################


# Grid format:
#   0 = Navigable space
#   1 = Occupied space



grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]]

heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search():
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed[init[0]][init[1]] = 1
    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    
    x = init[0]
    y = init[1]
    g = 0
    h = heuristic[x][y]
    f = g + h
    
    open = [[f,g,h,x,y]]
    
    found = False   #flag that is set when search completes 
    resign = False  #flag i sset when we cant expand
    count = 0
    
    print('Initial Open list:')
    for i in range(len(open)):
        print(' ', open[i])
    print('......')
    
    while found is False and resign is False:
        if len(open) == 0:
            resign = True 
            print('Fail') 
            #when no elements in open list
            
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            g = next[1]
            x = next[3]
            y = next[4]
            expand[x][y] = count
            count = count + 1
            
            if x == goal[0] and y ==goal[1]:
                found = True
                print (next)
                
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):        #grid is accessible and robot can move 
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:                       #not yet checked & grid cell is navigable
                            g2 = g + cost
                            h2 = heuristic[x2][y2]
                            f2 = g2 + h2
                            open.append([f2,g2,h2,x2,y2])
                            closed[x2][y2] = 1
                            
    for i in range(len(expand)):
        print(' ', expand[i])

search()

##################################################################################################################################################

# This example illustrates the search algorithm in a given grid world and goal location. 

# OBJECTIVE - Write a program that finds the shortest path that leads the robot from the start state to the goal state. 

# GIVEN - 
# The grid world can be a parking structure and you want to move the robot to its goal location. For simplicity, robot can move in 4 directions. 
# Three variables i.e. x,y & g where x,y are the grid dimensions and g is the shortest distance to the goal state. 
# Let us assume that the robot takes certain actions with certainity. 

###################################################################################################################################################


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search():
   
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]   #makes a 2x2 array similar to the grid array
    closed[init[0]][init[1]] = 1                                                #intital position defined
    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    
    
    x = init[0]
    y = init[1]
    g = 0
    
    open = [[g,x,y]]
    
    found = False #flag that is set when search completes 
    resign = False #flag i sset when we cant expand
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
            # remove node from list
            open.sort()
            open.reverse()
            next = open.pop() # pops the smallest number from the list
            g = next[0]
            x = next[1]
            y = next[2]
            expand[x][y] = count #This helps in constructing the table for printing
            count = count + 1
            
            # check if we are done and found the goal state
            if x == goal[0] and y ==goal[1]:
                found = True
                print (next)
                
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]): #grid is accessible and robot can move 
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0: #not yet checked & grid cell is navigable
                            g2 = g + cost
                            open.append([g2,x2,y2])
                            closed[x2][y2] = 1
                            
  #return path
    for i in range(len(expand)):
        print(' ', expand[i])

search()

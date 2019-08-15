###########################################################################################################################################
# This example illustrates the particle filter algorithm in a 4 point landmark 

# OBJECTIVE - Write a program that will iteratively assign weights to 1000 particles and illustrate the working of particle filter
# GIVEN 
# Four landmarks in the 100x100 world

###########################################################################################################################################

from math import *
import random

landmarks  = [[20.0, 20.0], [80.0, 80.0], [20.0, 80.0], [80.0, 20.0]]  # 4 points located in 100x100 world size 
world_size = 100.0


class robot:
    def __init__(self):
        self.x = random.random() * world_size
        self.y = random.random() * world_size
        self.orientation = random.random() * 2.0 * pi
        self.forward_noise = 0.0;
        self.turn_noise    = 0.0;
        self.sense_noise   = 0.0;
    
    # sets x,y and orientation of the particles
    def set(self, new_x, new_y, new_orientation):
        if new_x < 0 or new_x >= world_size:
            raise ValueError('X coordinate out of bound')
        if new_y < 0 or new_y >= world_size:
            raise (ValueError, 'Y coordinate out of bound')
        if new_orientation < 0 or new_orientation >= 2 * pi:
            raise (ValueError, 'Orientation must be in [0..2pi]')
        self.x = float(new_x)
        self.y = float(new_y)
        self.orientation = float(new_orientation)
    
    # function to set noise 
    def set_noise(self, new_f_noise, new_t_noise, new_s_noise):
        # makes it possible to change the noise parameters
        # this is often useful in particle filters
        self.forward_noise = float(new_f_noise);
        self.turn_noise    = float(new_t_noise);
        self.sense_noise   = float(new_s_noise);
    
    # function for robot to sense the envirnmeent 
    def sense(self):
        Z = []
        for i in range(len(landmarks)):
            dist = sqrt((self.x - landmarks[i][0]) ** 2 + (self.y - landmarks[i][1]) ** 2)
            dist += random.gauss(0.0, self.sense_noise)
            Z.append(dist)
        return Z
    
    
    def move(self, turn, forward):
        if forward < 0:
            raise (ValueError, 'Robot cant move backwards')        
        
        # turn, and add randomness to the turning command
        orientation = self.orientation + float(turn) + random.gauss(0.0, self.turn_noise)
        orientation %= 2 * pi
        
        # move, and add randomness to the motion command
        dist = float(forward) + random.gauss(0.0, self.forward_noise)
        x = self.x + (cos(orientation) * dist)
        y = self.y + (sin(orientation) * dist)
        x %= world_size    # cyclic truncate
        y %= world_size
        
        # set particle
        res = robot()
        res.set(x, y, orientation)
        res.set_noise(self.forward_noise, self.turn_noise, self.sense_noise)
        return res
    
    def Gaussian(self, mu, sigma, x):
        
        # calculates the probability of x for 1-dim Gaussian with mean mu and var. sigma
        return exp(- ((mu - x) ** 2) / (sigma ** 2) / 2.0) / sqrt(2.0 * pi * (sigma ** 2))
    
    # defines a random gaussian probability for weights calculation 
    def measurement_prob(self, measurement):
        
        # calculates how likely a measurement should be
        
        prob = 1.0;
        for i in range(len(landmarks)):
            dist = sqrt((self.x - landmarks[i][0]) ** 2 + (self.y - landmarks[i][1]) ** 2)
            prob *= self.Gaussian(dist, self.sense_noise, measurement[i])
        return prob
    
    
    
    def __repr__(self):
        return '[x=%.6s y=%.6s orient=%.6s]' % (str(self.x), str(self.y), str(self.orientation))

myrobot = robot()

N = 1000 # 1000 particles in the space
T = 100 # loop value
p = [] # list of particles with noise 
p2 = [] # list of particles with an orientation defined in the program. 
weight = []   #list of weights that contains the weights of the particles which have more importance. 
for i in range(N):
    r = robot()
    r.set_noise(0.05, 0.05, 5.0)
    p.append(r)

for t in range(T):
    myrobot = myrobot.move(0.1,5.0)
    Z = myrobot.sense()

    for i in range(N):
        p2.append(p[i].move(0.1,5.0))
    p = p2

    for i in range(N):
        weight.append(p[i].measurement_prob(Z))  # measurement_prob provides random gaussian probabilities to the particles. 

    # This section uses resampling for efficient working of particle filters. 
    p3 = []
    index = int(random.random() * N)
    beta = 0.0
    max_weight = max(weight)
    for i in range(N):
        beta += random.random() * 2.0 * max_weight
        while beta > weight[index]:
            beta -= weight[index]
            index = (index + 1) % N
        p3.append(p[index])
    p = p3
print(p)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practical 8 Animation and Behaviour, Agent Class, based on GEOG5995 learning materials. 

@author: nastazjalaskowski
"""
# Import relevant libraries first.

import random

"""
The code below contains an Agent class to define an agent in an environment.

environment: list of imported data defining the agent's environment.
y/x: the coordinates of the agent in the environment. 
store: contains the 'food'(data) the agent has eaten. 
neighbourhood: the distance agents need to be within each other to share stored 'food'.


The functions define the agent's behaviour. 

move: x and y coordinates of the agent change randomly by + or - 1. 
eat: agents deplete 'food' (data) from the environment and add to their own store at their location.
share_with_neighbours: when agents are within neighbourhood distance of each
other they evenly share their 'food' stores.
    
"""

# Set up the Class for agents (using a constructor method.)
# def __init__ can take three arguments besides 'self': the environment data, 
# list of agents and the neighbourhood. random.randint sets the y and x coordinates
# as a random integer within the provided parameters.

class Agent:

    def __init__(self, environment, agents, neighbourhood):
        self.y = random.randint(0,300)
        self.x = random.randint(0,300)
        self.environment = environment
        self.agents = agents
        self.neighbourhood = neighbourhood
        self.store = 0
     
        
# Make a move method within Agent class.   
# % is a Torus boundary solution creating a doughnut effect so that agents
# stay within the boundaries of the plotted graphs.
          
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 300 
        else:
            self.y = (self.y - 1) % 300

        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300
            
# Make an eat method where agents eat the environment by 10 if there is >10 food left.

    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            
# Make a method where agents search for close neighbours and share resources with them.

    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                avg = sum /2
                self.store = avg
                agent.store = avg
                # use print to check if it is running
                # print("sharing " + str(dist) + " " + str(avg))
                
# Pythagoras code used for the method above.
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
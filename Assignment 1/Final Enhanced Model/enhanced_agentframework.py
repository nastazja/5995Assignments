#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enhanced Agent Class Framework, based on GEOG5995 Learning Materials

@author: nastazjalaskowski
"""
# Import relevant libraries. 

import random

'''

The code below contains an Agent class to define an agent in an environment.

environment: list of imported data defining the agent's environment.
y/x: the coordinates of the agent in the environment. 
store: contains the 'food'(data) the agent has eaten. 
neighbourhood: the distance agents need to be within each other to share stored 'food'.


The methods below define the agent's behaviour. 

move: x and y coordinates of the agent change randomly by + or - 1. 
eat: agents deplete 'food' (data) from the environment and add to their own store at their location.
share_with_neighbours: when agents are within neighbourhood distance of each
other they evenly share their 'food' stores.
    
'''

# Set up the Class for agents (using a constructor method.)
# def __init__ can take three arguments besides 'self': the environment data, 
# list of agents and the neighbourhood. random.randint sets the y and x coordinates
# at a random integer between the specified parameters if no other value is provided.

class Agent:
    
    def __init__(self, environment, agents, neighbourhood, y=None, x=None):
        self.y = y
        self.x = x
        self.environment = environment
        self.agents = agents
        self.neighbourhood = neighbourhood
        self.store = 0
       
        if (x == None):
            self.x = random.randint(0,300)
        else:
            self.x = x
            
        if (y == None):
            self.y = random.randint(0,300)
        else:
            self.y = y
        
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
            
# Make an eat method where agents eat the environment by 10 if there is >10 food left,
# else eat whatever food value is left. 
 
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else: 
            self.environment[self.y][self.x] -= self.environment[self.y][self.x]
            self.store += self.environment[self.y][self.x]
            
# Calculate the distance between agents using Pythagoras.

    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
            
# Make a share method where agents search for close neighbours 
# and share resources with them.

    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            if self != agent: # to prevent agents comparing with themself.
                if self.distance_between(agent) <= neighbourhood:
                    avg = (self.store + agent.store)/2
                    self.store = avg
                    agent.store = avg
                #print("sharing " + str(self.distance_between(agent)) + " " + str(avg))
     
# The __str__ method allows easy printing of agent locations and stores. 

    def __str__(self):
        return (str(self.x) + "," + str(self.y) + " " + "stores" + " " + str(self.store))
                
    

'''
The code below contains a Wolves class to define a wolf in the animation. 

y/x: the coordinates of the wolf. 
store: contains the data the wolf absorbs after eating an agent. 
wolf_hood: the distance wolves need to be in relation to agents to eat them. 


The methods below define the wolf's behaviour. 

move: x and y coordinates of the wolf change randomly by + or - 1. 
eat_agent: the wolf removes an agent from the environment and adds the agent's store to its own.
   
'''
 

# Set up the Class for wolves using a constructor method. The y and x coordinates
# are a random integer between 0 and 300 that change by + or - 1 randomly with each
# iteration. 
               
class Wolves:
    def __init__(self, wolves, wolf_hood, agents):
        self.y = (random.randint(0,300))
        self.x = (random.randint(0,300))
        self.wolves = wolves
        self.wolf_hood = wolf_hood
        self.agents = agents
        self.store = 0
    
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 300 # % is the Torus boundary solution. 
        else: 
            self.y = (self.y - 1) % 300 
            
        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300
            
# The eat_agent method evaluates whether agents are in the wolf's neighbourhood
# ie. the 'wolf_hood' and if so, the agent is removed and the wolf absorbs its stores.
            
    def eat_agent(self, wolves, agents, wolf_hood):
     for wolf in self.wolves:
        for agent in self.agents:
            wolves_dist = self.distance_between(agent)
            if wolves_dist <= wolf_hood:
                self.store += agent.store
                agents.remove(agent)
                    
# Distance between the wolf and agent is measured using Pythagoras theorum. 

    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + (self.y - agent.y)**2)**0.5 
    
# The __str__ method allows easy printing of wolf locations and stores. 

    def __str__(self):
        return (str(self.x) + "," + str(self.y) + " " + "stores" + " " + str(self.store))


'''
End of Enhanced Agent Class Framework.
'''
                
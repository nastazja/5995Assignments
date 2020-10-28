#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 16:05:56 2020

@author: nastazjalaskowski
"""
import random

# Set up a Class.
class Agent:
    
# Set up variables x and y for the agent (random numbers).
    def __init__(self, environment, agents):
        self.environment = environment
        self.agents = agents
        self.store = 0
        self.y = random.randint(0,295)
        self.x = random.randint(0,295)
        
# Make a move method within Agent class. Must be in its own place (no indent).           
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 300 
        else:
            self.y = (self.y - 1) % 300

        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300
            
# Make the agents eat the environment. 
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
    

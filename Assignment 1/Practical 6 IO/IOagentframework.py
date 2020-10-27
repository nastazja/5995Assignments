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
    def __init__(self, environment):
        self.environment = environment
        self.store = 0
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)
        
# Make a move method within Agent class. Must be in its own place (no indent).           
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100 
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
            
# Make the agents eat the environment. 
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            

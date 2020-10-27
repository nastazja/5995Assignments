#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 12:15:56 2020

@author: nastazjalaskowski
"""
import matplotlib.pyplot
import prac5agentframework

# Convince yourself prac5model.py and prac5agentframework.py are connected.
a = prac5agentframework.Agent()
print(a.y, a.x)
a.move()
print(a.y, a.x)

# Make a function declaration for the function which will measure distance between coordinates. 
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5

# Add a variable that will control how many agents we have.
num_of_agents = 10 

# Add a variable that will change our agents coordinates an arbitrary number of times.
num_of_iterations = 100

# Create a list for our agents.
agents = []

# Use a for-loop to create as many agents as we like. 
for i in range(num_of_agents):
    agents.append(prac5agentframework.Agent())

# Make a fresh for-loop to move all agents. 
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        
        agents[i].move()
            

# Plot agent locations
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

# Measure distance between agents. 
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)


#End of Practical 5: Classes, Objects and Agents.  



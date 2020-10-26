#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 12:15:56 2020

@author: nastazjalaskowski
"""
import random
# import operator (not used in this practical)
import matplotlib.pyplot

# Add a variable that will control how many agents we have.
num_of_agents = 10 

# Add a variable that will change our agents coordinates an arbitrary number of times.
num_of_iterations = 100

# Create a list for our agents.
agents = []

# Use a for-loop to create as many agents as we like. 
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

# Make a fresh loops to move all agents. Add torus solution for boundary effects (makes the area into a doughnut shape, fine for abstract data).
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100
            
'''
Can't measure distance between agents by Pythagoras theorum right now as the earlier equation uses 2 sets of coordinates only.
answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print(answer).

To find out which agent is furthest east (largest x value) we would need to pass
in an extra function to access the second element of the list.
print(max(agents, key=operator.itemgetter(1))) '''

# Plot agent locations
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

'''#Colour the most easterly point red. This plots the point a second time.
m = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(m[1],m[0], color='red')'''


#End of Practical 3: Branching, Loops and Code Shrinking II. 



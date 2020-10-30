#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 12:15:56 2020

@author: nastazjalaskowski
"""
import random
# import operator (not used in this practical)
import matplotlib.pyplot
from time import perf_counter

''' Make a function declaration for the function which will measure distance between coordinates. 
We use agents_row_a[0] rather than agents_row_a[0][0] because agents_row_a already refers to agents[0]
so we can drop one dimension'''
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5

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
            
''' To find out which agent is furthest east (largest x value) we would need to pass
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

distance = distance_between(agents[0], agents[1])
print(distance) 

# Start timer for comparison of agents against each other. time.clock() has been deprecated since Python 3.3 so tried perf_counter instead.
start = perf_counter()

# Build for loop structure that tests every agent against every other agent and time the procedure. j+1 prevents repeats of agents.
for j in range(num_of_agents):
    for i in range(j+1, num_of_agents):
        distance = distance_between(agents[j], agents[i])
        print(distance)
        
# Finish timer. 
end = perf_counter()

# Print time taken.
print("time = " + str(end - start))

#End of Practical 4: Functions and Building Tools.  



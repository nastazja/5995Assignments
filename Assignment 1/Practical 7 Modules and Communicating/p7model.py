#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 12:15:56 2020

@author: nastazjalaskowski
"""
import matplotlib.pyplot
import p7agentframework
import csv
import random 

# Add a variable that will control how many agents we have.
num_of_agents = 10 

# Add a variable that will change our agents coordinates an arbitrary number of times.
num_of_iterations = 100

# Add neighbourhood variable.
neighbourhood = 20 

# Create a list to contain 2D data from in.txt for the environment.
environment = []

# Create a list for our agents.
agents = []

# Read in environment data from in.txt.
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

# Sort in.txt into rows and after this is finished, append to environment.
for row in reader:				
    rowlist = [] 
    for value in row:		
        rowlist.append(value)
    environment.append(rowlist)
f.close()

# Use a for-loop to create as many agents as we like. 
for i in range(num_of_agents):
    agents.append(p7agentframework.Agent(environment, agents))
    
# Shuffle the agents each iteration before they do their stuff.
for j in range(num_of_iterations):
    random.shuffle(agents)

# Make a fresh for-loop to move all agents. 
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
            
# Plot agent locations and display our environment.
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

# Write environment as file at end.
f2 = open('dataout.csv', 'w', newline='') 
writer = csv.writer(f2, delimiter=',')
for row in environment:		
	writer.writerow(row)		
f2.close()

#End of Practical 7: Modules and Communicating.



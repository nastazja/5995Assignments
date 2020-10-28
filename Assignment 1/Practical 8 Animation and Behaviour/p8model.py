#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 12:15:56 2020

@author: nastazjalaskowski
"""
import matplotlib
matplotlib.use('Qt5Agg')

import matplotlib.pyplot
import p8agentframework
import csv
import random 
import matplotlib.animation

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

# Define the figure for animating. 
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
#ax.set_autoscale_on(False)

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
    agents.append(p8agentframework.Agent(environment, agents))
    
# Shuffle the agents each iteration before they do their stuff.
for j in range(num_of_iterations):
    random.shuffle(agents)
    
carry_on = True
    
def update(frame_number):
    fig.clear()
    global carry_on 

# Make a fresh for-loop to move all agents. 
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
        
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
            
    for i in range(num_of_agents):    
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
        matplotlib.pyplot.imshow(environment)
        
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
            
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

matplotlib.pyplot.show()

# Write environment as file at end.
f2 = open('dataout.csv', 'w', newline='') 
writer = csv.writer(f2, delimiter=',')
for row in environment:		
	writer.writerow(row)		
f2.close()


#End of Practical 8: Animation and Behaviour. 



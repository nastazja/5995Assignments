#!/usr/bin/env python3
"""
Practical 8: Animation and Behaviour, ABM, based on GEOG5995 learning materials.

@author: nastazjalaskowski


The first section of code groups together all the imports, variables and lists
from the programme for easy reference. 

"""


# Import all the required packages first. 

import matplotlib
matplotlib.use('Qt5Agg') # allows selection of backend needed for graphics to work.
import p8agentframework # needed to access Agent class and methods.
import matplotlib.pyplot # creates figures with agent coordinates and environment.
import csv # reads in file with environment data.
import random # needed to shuffle agents.
import matplotlib.animation # creates animantion of agents. 


# List all variables that can be altered at the top. 

num_of_agents = 10 # controls how many agents we have.
num_of_iterations = 100 # changes agents coordinates an arbitrary number of times.
neighbourhood = 20 # definition of distance classified 'neighbourhood'.

# Create empty lists. 

environment = []  # to contain 2D data from in.txt for the environment.
agents = [] # to contain our agents. 

"""
The code below initiates and runs the Agent Based Model where agents move, eat
and share 'food' (data). The output is a GUI with animated figure. 

"""


# CREATE ENVIRONMENT:

# Read in environment data from in.txt.

f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

# Sort in.txt into rows and after this is finished, append to environment list.

for row in reader:				
    rowlist = [] 
    for value in row:		
        rowlist.append(value)
    environment.append(rowlist)
f.close()


# CREATE AGENTS: 
    
# Use a for-loop to create as many agents as we like. 
for i in range(num_of_agents):
    agents.append(p8agentframework.Agent(environment, agents, neighbourhood))
    
# Shuffle the agents each iteration before they do their stuff.
for j in range(num_of_iterations):
    random.shuffle(agents)
    

# CREATE ANIMATION:
    
carry_on = True #boolean for stopping condition. 

# Define the figure for animating. 

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
#ax.set_autoscale_on(False)

# Define a function as input for the animation. 
    
def update(frame_number):
    fig.clear()
    global carry_on 

# Make a fresh for-loop to move all agents and initiate eat and share behaviours.

    for j in range(num_of_iterations):
        for i in range(num_of_agents):
        
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            
    if random.random() < 0.1: # a random stop condition taken from learning materials.
        carry_on = False
        print("stopping condition")
            
    for i in range(num_of_agents):    
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y) # plots coordinates.
        matplotlib.pyplot.imshow(environment)
        
# Make a function that acts as an iterator:
    
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        
# Produce the animation.
            
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
matplotlib.pyplot.show()


# DATA OUTPUT: 
    
# Write environment as file at end.
f2 = open('dataout.csv', 'w', newline='') 
writer = csv.writer(f2, delimiter=',')
for row in environment:		
	writer.writerow(row)		
f2.close()


"""
END OF PRACTICAL 8: ANIMATION AND BEHAVIOUR.

"""

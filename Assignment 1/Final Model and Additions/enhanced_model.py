#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practical 9 ABM Model, based on GEOG5995 Learning Materials

@author: nastazjalaskowski
"""

'''

The code in this first section groups together all the imports, variables and lists
from the programme for easy reference. 

'''

# Import all the required packages first. 

import matplotlib
matplotlib.use('TkAgg') # allows selection of backend needed for graphics to work.
import enhanced_agentframework # needed to access Agent class and methods.
import matplotlib.pyplot # creates figures with agent coordinates and environment.
import csv # reads in file with environment data.
import random # needed to shuffle agents.
import matplotlib.animation # creates animantion of agents. 
import tkinter # builds GUI. 

# List all variables that can be altered at the top. 

num_of_agents = 10 # controls how many agents we have.
num_of_iterations = 100 # changes agents coordinates an arbitrary number of times.
neighbourhood = 20 # definition of distance classified 'neighbourhood'.

# Create empty lists. 

environment = []  # to contain 2D data from in.txt for the environment.
agents = [] # to contain our agents. 

# Create stopping condition variables.

counter = 0 # to keep track of iterations.


'''

The code below initiates and runs the Agent Based Model where agents move, eat
and share 'food' (data). The output is a GUI with animated figure. 

'''

# Define the figure for animating. 

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
#ax.set_autoscale_on(False)


# SET UP ENVIRONMENT:
    
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


# CREATE AGENTS AND INTIATE BEHAVIOURS:
    
# Use a for-loop to create as many agents as we like. 

for i in range(num_of_agents):
    agents.append(enhanced_agentframework.Agent(environment, agents, neighbourhood))
    
carry_on = True # boolean to stopping condition.
    
def update(frame_number): # animation set-up.
    fig.clear()
    global carry_on 
    global counter

# Make a fresh for-loop to move all agents and initiate behaviours.
    for j in range(num_of_iterations):
        random.shuffle(agents) # shuffle agents in each iteration before they act.
        for i in range(num_of_agents):
        
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            
# Define stopping conditions. 
        
    if counter == (num_of_iterations):
        carry_on = False
        print("STOP - iterations completed")
    else:
        counter += 1
        
        
# PLOT COORDINATES AND MAKE ANIMATION: 
 
# Plot x and y coordinates in the environment. 

    for i in range(num_of_agents):    
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
        matplotlib.pyplot.imshow(environment)
        matplotlib.pyplot.xlim(0, 300)
        matplotlib.pyplot.ylim(0, 300)
    
# Supply data to the animation. 
     
def gen_function(misc = []):
    global carry_on 
    global counter
    while carry_on:
        yield counter
        
        
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=10, frames=gen_function, repeat=False)
#matplotlib.pyplot.show()


# MAKE A GUI: 
      
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, interval = 10, frames=gen_function, repeat=False)
    canvas.draw()
            
root = tkinter.Tk()   
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
tkinter.mainloop()


# OUTPUT FILE:

# Write environment as file at the end of the programme. 

f2 = open('envout.csv', 'w', newline='') 
writer = csv.writer(f2, delimiter=',')
for row in environment:		
	writer.writerow(row)		
f2.close()
























#End of Practical 9: GUI and Web. 



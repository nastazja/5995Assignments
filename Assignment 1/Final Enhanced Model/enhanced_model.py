#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enhanced ABM, based on GEOG5995 Learning Materials

@author: nastazjalaskowski
"""

'''

The code in this first section groups together all the imports, variables and lists
from the programme for easy reference. 

'''

# Import all the required packages first. 

import matplotlib
matplotlib.use('TkAgg') # allows selection of backend needed for graphics to work.
import enhanced_agentframework # needed to access Agent/Wolves class and methods.
import matplotlib.pyplot # creates figures with agent/wolf coordinates and environment.
import csv # reads in file with environment data.
import random # needed to shuffle agents.
import matplotlib.animation # creates animantion of agents. 
import tkinter # builds GUI. 
import requests # needed to scrape website.
import bs4 # pulls data out of HTML. 

'''
sys.argv can be used to run the file from command line with custom parameters.
eg. enhanced_model.py 30 100 20 5 10. In which case the code below would need to
be inserted instead of defining the parameters within the code:
    
    import sys
    num_of_agents = int(sys.argv[1])
    num_of_iterations = int(sys.argv[2])
    neighbourhood = int(sys.argv[3])
    num_of_wolves = int(sys.argv[4])
    wolf_hood = int(sys.argv[5])
    
The following programme defines the parameters within the code:
    
'''

# List all variables that can be altered within the code at the top. 

num_of_agents = 30 # controls how many agents we have.
num_of_iterations = 100 # changes agents coordinates an arbitrary number of times.
neighbourhood = 20 # defines distance classified as 'neighbourhood'.
num_of_wolves = 5 # controls how many wolves we have.
wolf_hood = 10 # defines proximity needed for wolves to eat agents.

# Create empty lists. 

environment = []  # to contain 2D data from in.txt for the environment.
agents = [] # to contain our agents. 
wolves = [] # to contain our wolves. 

# Create stopping condition variables.

counter = 0 # to keep track of iterations.

'''

The code below initiates and runs the Agent Based Model where agents move, eat
and share 'food' (data). Wolves eat agents and absorb their stores.
The output is a GUI with animated figure and a file for the environment.

'''
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

# CREATE AGENTS:

# Import data for the agents from the web.

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
# print(td_ys)
# print(td_xs)

# Use a for-loop to create as many agents as we like. 

for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(enhanced_agentframework.Agent(environment, agents, neighbourhood, y, x))
    
    
# CREATE WOLVES:
    
# Use a for-loop to create as many wolves as we like. 
    
for j in range(num_of_wolves):
    wolves.append(enhanced_agentframework.Wolves(wolves, wolf_hood, agents))
    
    
# SET UP ANIMATION:
    
# Define the figure for animating. 

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
#ax.set_autoscale_on(False)
    
carry_on = True # boolean to stopping condition.
    
def update(frame_number): # animation set-up.
    fig.clear()
    global carry_on 
    global counter


# INITIATE AGENT BEHAVIOURS:

# Make a fresh for-loop to move all agents and initiate behaviours move, eat and share
# as defined by the Agent class.

    for j in range(num_of_iterations):
        random.shuffle(agents) # shuffle agents in each iteration before they act.
        for i in range(len(agents)):
        
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            
# Define stopping conditions (completion of iterations).
        
    if counter == (num_of_iterations):
        carry_on = False
        print("STOP - iterations completed")
    else:
        counter += 1
        
        
# PLOT COORDINATES OF AGENTS IN ANIMATION: 
 
# Plot x and y coordinates of agents in the environment. 

    for i in range(len(agents)):    
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y, color= 'white')
        
        
# INITIATE BEHAVIOUR OF WOLVES: 

# Make a for-loop that will initiate behaviours move and eat_agent as defined
# by the Wolves class.
    
    for j in range(num_of_iterations):
        random.shuffle(wolves) # shuffle wolves in each iteration before they act.
        for m in range(len(wolves)):
            wolves[m].move()
            wolves[m].eat_agent(wolves, agents, wolf_hood)
            
            
# PLOT COORDINATES OF WOLVES IN ANIMATION:

# Plot x and y coordinates of wolves in the environment. 
    
    for i in range(len(wolves)):
        matplotlib.pyplot.scatter(wolves[i].x, wolves[i].y, color= 'black')
     
    matplotlib.pyplot.imshow(environment)
    matplotlib.pyplot.xlim(0, 300) # sets the x-axis
    matplotlib.pyplot.ylim(0, 300) # sets the y-axis
     
# Supply data to the animation. 
     
def gen_function(misc = []):
    global carry_on 
    global counter
    while carry_on:
        yield counter
        
# The code below produces an animation figure without GUI when commented in.
        
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=10, frames=gen_function, repeat=False)
#matplotlib.pyplot.show()
#animation.save('ABM_animation.mp4', fps=60)


# MAKE A GUI (code taken from the lectures, creates a pop-up. Sometimes glitchy 
# and creates two pop ups). 
      
def run(): # will initiate the animation when Menu -> Run model is clicked.
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

# Build the layers and labels of the GUI and link it to the run method.

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

# Print coordinates and stores of agents and wolves, enhanced_agentframework contains
# __str__ method to simplify this.

for i in range (len(agents)):
    print(agents[i])
    
for j in range (len(wolves)):
    print(wolves[j]) 

    
'''
End of Enhanced ABM.
'''

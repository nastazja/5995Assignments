#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 12:15:56 2020

@author: nastazjalaskowski
"""
import random
import operator 
import matplotlib.pyplot

# Create a list for our agents.
agents = []

''' Removed:
y0 = random.randint(0,99)
x0 = random.randint(0,99)

Instead of making variables y0 and x0 for this short time, we can put
[randomrandint(0,99), randomrandint(0,99)] straight into agents.append to 
resemble y0 and x0.

Square brackets add coordinates as a list inside another list.'''

# Add y0 and x0 to our agents list.
agents.append([random.randint(0,99),random.randint(0,99)])

# Build code that will alter y randomly. 
if random.random() < 0.5:
    agents[0][0] += 1
else:
    agents[0][0] -= 1
    
# Alter x randomly.
if random.random() <0.5:
    agents[0][1] += 1
else:
    agents[0][1] -= 1
    
print([agents[0][0],agents[0][1]])

#Add y1 and x1 to our agents. 
agents.append([random.randint(0,99),random.randint(0,99)])

if random.random() < 0.5:
    agents[1][0] += 1
else:
    agents[1][0] -= 1
    
if random.random() <0.5:
    agents[1][1] += 1
else:
    agents[1][1] -= 1
    
print([agents[1][0],agents[1][1]])


'''
Measure distance between agents by Pythagoras theorum...
answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print(answer)
'''

# The function print(max(agents)) would print the coordinates with the biggest y value. 

''' To find out which agent is furthest east (largest x value) we need to pass
in an extra function to access the second element of the list. '''

print(max(agents, key=operator.itemgetter(1)))

''' Next we are going to plot our agent locations in a graph using 
matplotlib.pyplot'''

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])

#Colour the most easterly point red. This plots the point a second time.
m = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()


#End of Practical 2: Containers and Code Shrinking I. 



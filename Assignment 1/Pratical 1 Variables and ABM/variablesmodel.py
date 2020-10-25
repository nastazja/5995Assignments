#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 12:15:56 2020

@author: nastazjalaskowski
"""
import random

'''Make two variables y0 and x0 and assign them the values 50 and 50.
y0 = 50
x0 = 50
print (y0, x0)'''

# Instead we will make two variables y0 and x0 with random start points.
y0 = random.randint(0,99)
x0 = random.randint(0,99)

# Build code that will alter y randomly. 
'''random.random generates a random floating point number within the range zero 
to just less than one. You can multiple it by 100 to generate a float between 
0 and just less than 100. There's also a random.randint(start,end) function 
that will generate int values between 'start' and 'end' (inclusive)'''

if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1
    
# Alter x randomly.
if random.random() <0.5:
    x0 += 1
else:
    x0 -= 1
    
print(y0,x0)

'''the above code could be condensed but then it binds the movement of y0 and
x0 together (either both go up or both go down)'''

# Create a second set of steps.
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1
    
# Alter x randomly
if random.random() <0.5:
    x0 += 1
else:
    x0 -= 1
    
print(y0,x0)

'''Make a second agent by copying the code above and renaming the variables
to y1 and x1. '''

y1 = random.randint(0,99)
x1 = random.randint(0,99)

if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1
    
if random.random() <0.5:
    x1 += 1
else:
    x1 -= 1
    
print(y1,x1)

if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1
    
# Alter x randomly
if random.random() <0.5:
    x0 += 1
else:
    x0 -= 1
    
print(y1,x1)

'''Work out the Euclidian (straight-line) distance between the two sets of 
coordinates using Pythagoras' theorem '''

answer = (((y0-y1)**2) + ((x0-x1)**2) **0.5)
print(answer)

#End of variables Practical 1.



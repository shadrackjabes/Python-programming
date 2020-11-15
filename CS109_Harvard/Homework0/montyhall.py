#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 23:57:04 2020

@author: shadrack
"""
import numpy as np
import math

def simulate_prizedoor(nsim):
    """
Function
--------
simulate_prizedoor

Generate a random array of 0s, 1s, and 2s, representing
hiding a prize between door 0, door 1, and door 2

Parameters
----------
nsim : int
    The number of simulations to run

Returns
-------
sims : array
    Random array of 0s, 1s, and 2s

Example
-------
>>> print simulate_prizedoor(3)
array([0, 0, 2])
    """
    ndoors=3
    doors=np.arange(1,ndoors+1)
    sims = np.random.rand(nsim)*len(doors)
    
    for j in range(len(sims)):
        
        for i in range(len(doors)):
            if(i==0):
                if(sims[j]<doors[i]):
                    sims[j] = i
            else:
                if(sims[j]<doors[i]):
                    if(sims[j]>doors[i-1]):
                        sims[j] = i
    
    print("prize"+str(sims))
    return(sims)
    
def simulate_guess(nsim):
    """
Function
--------
simulate_guess

Return any strategy for guessing which door a prize is behind. This
could be a random strategy, one that always guesses 2, whatever.

Parameters
----------
nsim : int
    The number of simulations to generate guesses for

Returns
-------
guesses : array
    An array of guesses. Each guess is a 0, 1, or 2

Example
-------
>>> print simulate_guess(5)
array([0, 0, 0, 0, 0])
    """
    ndoors=3
    doors=np.arange(1,ndoors+1)
    guess=np.ones(nsim)
    
    for i in range(nsim):
        A=np.random.rand(1)*len(doors)
        guess[i] = math.ceil(A)-1
    print("guess"+str(guess))
    return(guess)

def goat_door(price,guesses):
    """
Function
--------
goat_door

Simulate the opening of a "goat door" that doesn't contain the prize,
and is different from the contestants guess

Parameters
----------
prizedoors : array
    The door that the prize is behind in each simulation
guesses : array
    THe door that the contestant guessed in each simulation

Returns
-------
goats : array
    The goat door that is opened for each simulation. Each item is 0, 1, or 2, and is different
    from both prizedoors and guesses

Examples
--------
>>> print goat_door(np.array([0, 1, 2]), np.array([1, 1, 1]))
>>> array([2, 2, 0])
    """
    ndoors=3
    doors=np.arange(ndoors)
    goat=np.zeros(len(price))
    
    for j in range(len(price)):
        for i in range(len(doors)):
            if(price[j] != doors[i]):
                if(guesses[j] != doors[i]):
                    goat[j] = doors[i]
    #print("price"+str(price))
    #print("guesses"+str(guesses))
    print("goat"+str(goat))
    return(goat)

def switch_guess(guess,goat):
    """
Function
--------
switch_guess

The strategy that always switches a guess after the goat door is opened

Parameters
----------
guesses : array
     Array of original guesses, for each simulation
goatdoors : array
     Array of revealed goat doors for each simulation

Returns
-------
The new door after switching. Should be different from both guesses and goatdoors

Examples
--------
>>> print switch_guess(np.array([0, 1, 2]), np.array([1, 2, 1]))
>>> array([2, 0, 0])
    """
    ndoors=3
    doors=np.arange(ndoors)
    switchgoat=np.zeros(len(guess))
    
    for j in range(len(guess)):
        for i in range(len(doors)):
            if(goat[j] != doors[i]):
                if(guess[j] != doors[i]):
                    switchgoat[j] = doors[i]
    print("new guess"+str(switchgoat))
    return(switchgoat)

def win_percentage(guess,price):
    """
Function
--------
win_percentage

Calculate the percent of times that a simulation of guesses is correct

Parameters
-----------
guesses : array
    Guesses for each simulation
prizedoors : array
    Location of prize for each simulation

Returns
--------
percentage : number between 0 and 100
    The win percentage

Examples
---------
>>> print win_percentage(np.array([0, 1, 2]), np.array([0, 0, 0]))
33.333
    """
    ndoors=3
    doors=np.arange(ndoors)
    cnt1 = 0
    cnt2 = 0
    
    for i in range(len(guess)):
        if(guess[i] == price[i]):
            cnt1 += 1
        else:
            cnt2 += 1
    
    win_percentage=cnt1/(cnt1+cnt2)
    return(win_percentage*100.0)
    

"""
case1: Simulate 10000 games 
where contestant keeps his original guess, and 

case2: 10000 games 
where the contestant switches his door 
after a goat door is revealed. 

Compute the percentage of time 
the contestant wins under either strategy. 

Is one strategy better than the other?
"""
nsim = 10
price=simulate_prizedoor(nsim)
guess=simulate_guess(nsim)
goat=goat_door(price,guess)
val=win_percentage(guess,price)
print("method1 " +str(val))

nsim = 10
price=simulate_prizedoor(nsim)
guess=simulate_guess(nsim)
goat=goat_door(price,guess)
guess=switch_guess(guess,goat)
val=win_percentage(guess,price)
print("method2 " +str(val))

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 10:53:14 2021
Riddler Classic 20200918

One of Ollie’s favorite online games is Guess My Word. Each day, there is a secret word, and you try to guess it as efficiently as possible by typing in other words.
After each guess, you are told whether the secret word is alphabetically before or after your guess.
The game stops and congratulates you when you have guessed the secret word. For example, the secret word was recently “nuance,”
which Ollie arrived at with the following series of nine guesses: naan, vacuum, rabbi, papa, oasis, nuclear, nix, noxious, nuance.

Each secret word is randomly chosen from a dictionary with exactly 267,751 entries. If you have this dictionary memorized,
and play the game as efficiently as possible, how many guesses should you expect to make to guess the secret word?

@author: tae8858
"""
import random
import numpy as np
import math
import time

# Set up record of turns and possible dictionary
turn_rec = []
size = 267751
possible = np.arange(size)
sims = 1000000

start_time = time.time()
for i in range(sims):
    new_range = possible
    selection = random.choice(possible)
   # print("SELECTED: ", selection)
    
    # Reset number of turs taken
    turns = 1
    guess = math.trunc(len(possible)/2)
    #print("Guess number ", turns, " : ", guess)
    
    while guess != selection:
        turns += 1
        if guess < selection:
            new_range = np.arange(start = guess+1, stop = new_range[-1]+1)
        else:
            new_range = np.arange(start = new_range[0], stop = guess)
        guess = math.trunc(new_range[0] + len(new_range)/2)
        #print("Guess number ", turns, " : ", guess, "\tSelection: ", selection)
    turn_rec.append(turns)
print("Mean number of turns: ", sum(turn_rec)/len(turn_rec), " after ", sims, " simulations")
print("--- %s seconds ---" % (time.time() - start_time))
# Result : Mean number of turns:  17.041801  after  1000000  simulations
# Time : --- 433.2860379219055 seconds ---
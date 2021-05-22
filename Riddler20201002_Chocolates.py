# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 16:16:07 2021
Riddler Classic 02/10/2020
I have 10 chocolates in a bag: Two are milk chocolate, while the other eight are dark chocolate.
One at a time, I randomly pull chocolates from the bag and eat them — that is, until I pick a chocolate of the other kind.
When I get to the other type of chocolate, I put it back in the bag and start drawing again with the remaining chocolates.
I keep going until I have eaten all 10 chocolates.

For example, if I first pull out a dark chocolate, I will eat it. (I’ll always eat the first chocolate I pull out.)
If I pull out a second dark chocolate, I will eat that as well. If the third one is milk chocolate, I will not eat it (yet),
and instead place it back in the bag. Then I will start again, eating the first chocolate I pull out.

What are the chances that the last chocolate I eat is milk chocolate?

@author: tae8858
"""
import random

last = []
sims = 1000000

for i in range(sims):
    # Create bag, 8 dark chocolates and 2 milk chocolates, in random order
    bag = ['D' for i in range(8)] + ['M' for j in range(2)]
    random.shuffle(bag)
    
    prev = "None"
    # Create loop while there are more than one chocolate in bag
    while len(bag) > 1:
        # If same as previous, continue eating
        if bag[0]==prev:
            bag.pop(0)
        # If different, put back in and reset previous
        else:
            random.shuffle(bag)
            prev = bag[0]
            bag.pop(0)
        
    last.append(bag[0])

print("Chances last chocolate is milk: ", (last.count('M') / sims)*100, "%")
# Result : Chances last chocolate is milk:  49.9724 %
# Simulations to help approximate answer, analytical solution is much nicer and can prove 50%
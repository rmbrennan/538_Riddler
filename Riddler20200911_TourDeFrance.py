# -*- coding: utf-8 -*-
"""
Riddler Classic 20200911
For every mountain in the Tour de FiveThirtyEight, the first few riders to reach the summit are awarded points.
The rider with the most such points at the end of the Tour is named “King of the Mountains” and gets to wear a special polka dot jersey.

At the moment, you are racing against three other riders up one of the mountains. The first rider over the top gets 5 points,
the second rider gets 3, the third rider gets 2, and the fourth rider gets 1.

All four of you are of equal ability — that is, under normal circumstances, you all have an equal chance of reaching the summit first.
But there’s a catch — two of your competitors are on the same team. Teammates are able to work together, drafting and setting a tempo up the mountain.
Whichever teammate happens to be slower on the climb will get a boost from their faster teammate, and the two of them will both reach the summit at the faster teammate’s time.

As a lone rider, the odds may be stacked against you. In your quest for the polka dot jersey, how many points can you expect to win on this mountain, on average?

"""
# Import required packages and set seed
import random
import pandas as pd
import statistics
import time
random.seed(18858)

# Initiate values
sims = 100000
num_players = 4
points_pos = {1:5, 2:3, 3:2, 4:1}
player_points = []

# Wrap function with time
tic = time.perf_counter()
# Simulate races and 
for x in range(sims):
    temp_score = []
    for i in range(num_players):
        temp_score.append(random.random())
        
    new_score = pd.Series([temp_score[0], temp_score[1], max(temp_score[2:]), max(temp_score[2:])])
    ranks = new_score.rank(ascending=False)
    points = ranks.map(points_pos)
    player_points.append(points[0])
toc = time.perf_counter()

print("Number of simulations:\t\t\t\t", sims)
print("The average number of points:\t\t\t", statistics.mean(player_points))
print("Expected points if all independent:\t", statistics.mean([5, 3, 2, 1]))
print(f"Time taken: {toc - tic:0.2f} seconds")
# Result:
# Number of simulations:				 100000
# The average number of points:			 2.42483
# Expected points if all independent:	 2.75
# Time taken: 154.34 seconds
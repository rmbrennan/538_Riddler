# -*- coding: utf-8 -*-
"""
Created on Fri May 21 11:58:27 2021
Riddler Classic 30/10/2020
Instead of playing hot potato, you and 60 of your closest friends decide to play a socially distanced game of hot pumpkin.

Before the game starts, you all sit in a circle and agree on a positive integer N. Once the number has been chosen,
you (the leader of the group) start the game by counting “1” and passing the pumpkin to the person sitting directly to your left.
She then declares “2” and passes the pumpkin one space to her left. This continues with each player saying the next number in the sequence,
wrapping around the circle as many times as necessary, until the group has collectively counted up to N. At that point, the player who counted “N” is eliminated,
and the player directly to his or her left starts the next round, again proceeding to the same value of N. The game continues until just one player remains, who is declared the victor.

In the game’s first round, the player 18 spaces to your left is the first to be eliminated. Ricky, the next player in the sequence, begins the next round.
The second round sees the elimination of the player 31 spaces to Ricky’s left. Zach begins the third round, only to find himself eliminated in a cruel twist of fate. (Woe is Zach.)

What was the smallest value of N the group could have used for this game?

@author: tae8858
"""
x_range = 1000000
for i in range(x_range):
    if (i%61==19) and (i%60==32) and (i%59==1):
        print("Lowest possible N is :\t", i)
        N = i
        break
# Result : Lowest possible N is :	 136232    
#%%
"""
Extra credit: Suppose the players were numbered from 1 to 61, with you as Player No. 1, the player to your left as Player No. 2 and so on. Which player won the game?
"""
import numpy as np
print("Using N as ", N)
players = list(range(1,62))

while len(players) > 1:
    idx = N % len(players)-1
    player_out = players[(N % len(players))-1]
    players.pop((N % len(players))-1)
    players = list(np.roll(players, -idx if idx >=0 else 0))
    print("Ends on player ", idx if idx >= 0 else len(players), "positions to left.\t\tPlayer ", player_out, " removed")
print("Winner is player ", players, "!!!")
# Result : Winner is player  [58]
#%%
"""
Extra extra credit: What’s the smallest N that would have made you the winner?
"""
x_range = 50000000
possible_N = []
for i in range(x_range):
    if (i%61==19) and (i%60==32) and (i%59==1):
        possible_N.append(i)

# Assuming original starting order needs to be maintained
import numpy as np
for N in possible_N:
    players = list(range(1,62))
    
    while len(players) > 1:
        idx = N % len(players)-1
        player_out = players[(N % len(players))-1]
        players.pop((N % len(players))-1)
        players = list(np.roll(players, -idx if idx >=0 else 0))
    if players[0]==1:
        break
print("Using N as :", N, "\tWinner is player ", players)
# Result : Using N as : 42892352 	Winner is player  [1]

# Assuming original starting order does NOT need to be maintained
for N in range(1, x_range):
    players = list(range(1,62))
    
    while len(players) > 1:
        idx = N % len(players)-1
        player_out = players[(N % len(players))-1]
        players.pop((N % len(players))-1)
        players = list(np.roll(players, -idx if idx >=0 else 0))
    if players[0]==1:
        break
print("Using N as :", N, "\tWinner is player ", players)
# Result : Using N as : 140 	Winner is player  [1]
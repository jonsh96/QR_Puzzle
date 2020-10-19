import matplotlib.pyplot as plt
import math as math
import numpy as np
import player
import line
import random

# This file includes some helper functions

def plot_circles(board):
    # Plots each player as a circle on the line
    for p in board.players:
        x = p.midpoint
        y = 0 
        r = p.radius
        circ = plt.Circle((x,y), r, color=p.color)
        plt.gcf().gca().add_artist(circ)
        plt.text(x-0.01,y+0.01, p.name, fontsize=16)
        plt.plot(x,y, color=p.color, label="Player: {0}, Score: {1:.2f}".format(p.name, p.get_score()))
    # Plots the line
    plt.plot(np.array([0, 1]), np.array([0,0]), color="black", label=None)
    plt.xlim([0, 1])
    plt.ylim([0.0, 1.0])
    plt.legend()
    plt.grid()

def plot_scores(values, scores):
    # Plots the scores as a function of the values (i.e. points picked)
    plt.plot(values, scores, linestyle='dotted')
    plt.grid()
    plt.show()

def get_optimal_point(line, N):
    # Returns all possible points and the scores associated with them
    # Player name: A, B, ...
    player_name = chr(66+line.nr_players)
    values = []
    scores = []
    # Make a copy of the board
    players = line.players.copy()
    players.append(player.player(player_name, 0))
    nr_players = line.nr_players+1
    # Loop through all moves
    for i in range(0,N):
        # Loop through all players and change value
        for p in players:
            if p.name == player_name:
                # Add tiny noise to avoid picking exact same values
                p.value = i/N + np.random.normal(0,0.0005)
                values.append(p.value)
        # Sort players in terms of points picked (not midpoints)
        players = sorted(players)
        # Loops through all players and adjusts the midpoint
        for i in range(nr_players):
            # Edge case
            if(i == 0):
                prev = 0.0
                curr = players[i].value
                next = 0.5*(curr + players[i+1].value)
                players[i].midpoint = 0.5*(next-prev)
                players[i].radius = 0.5*(next-prev)
            else:
                prev = players[i-1].midpoint + players[i-1].radius    
                curr = players[i].value                               
                if(i == nr_players-1):
                    next = 1.0              
                else:
                    next = 0.5*(curr + players[i+1].value)       
                players[i].radius = 0.5*(next - prev)            
                players[i].midpoint = prev + players[i].radius
        # Gets the score of the given player
        for p in players:
            if p.name == player_name:
                scores.append(p.get_score())
    return values, scores

import player 
import numpy as np 

# This class is used to store the line as an object where you can add players and adjust the circles

class line:
    # Default constructor
    def __init__(self):
        self.start = 0.0
        self.end = 1.0
        self.nr_players = 0
        self.players = []
        self.colors = ["lightblue", "lightgreen", "red", "lightgrey", "orange", "aqua", "lightyellow"]

    # Add players
    def add_player(self, player):
        self.players.append(player)
        # Assign a colour to each player
        player.add_color(self.colors[self.nr_players])
        self.nr_players += 1
        # Sort players by value (small to large)
        self.players = sorted(self.players)
        # Adjust points and players
        self.adjust()

    def adjust(self):
        # Adjust midpoints and radius of each circle
        if(self.nr_players == 1):
            # Only one player => midpoint at 0.5 with a radius ranging the whole line
            self.players[0].midpoint = 0.5
            self.players[0].radius = 0.5
        else:
            # Multiple players
            for i in range(self.nr_players):
                # Edge case
                if(i == 0):
                    prev = 0.0
                    curr = self.players[i].value
                    next = 0.5*(curr + self.players[i+1].value)
                    self.players[i].midpoint = 0.5*(next-prev)
                    self.players[i].radius = 0.5*(next-prev)
                else:
                    prev = self.players[i-1].midpoint + self.players[i-1].radius    # Previous value
                    curr = self.players[i].value                                    # Current value
                    if(i == self.nr_players-1):
                        next = 1.0              
                    else:
                        next = 0.5*(curr + self.players[i+1].value)                 # Next end
                    self.players[i].radius = 0.5*(next - prev)                      # Distance between ends = 2*radius
                    self.players[i].midpoint = prev + self.players[i].radius

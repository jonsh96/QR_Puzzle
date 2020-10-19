# Stores each player as an object with a few properties (name, value, midpoint, radius and score)

class player:
    def __init__(self, name, value):
        # Default constructor
        self.name = name
        self.value = value
        self.midpoint = 0.0  
        self.radius = 0.0
        self.score = 0.0
        self.color = None

    def get_score(self):
        # Calculates and returns the score 
        self.score = 2*self.radius
        return self.score

    # Custom comparison operators 
    # - Needed to be able to sort by the players values 
    def __eq__(self, other):
        return (self.value == other.value)

    def __ne__(self, other):
        return (self.value != other.value)
        
    def __lt__(self, other):
        return (self.value < other.value)
        
    def __le__(self, other):
        return (self.value <= other.value)
        
    def __gt__(self, other):
        return (self.value > other.value)
        
    def __ge__(self, other):
        return (self.value >= other.value)
        
    def __str__(self):
        # Print function
        return "Player: {} chose point {} and is now at midpoint {} with a radius of {}\n".format(self.name, self.value, self.midpoint, self.radius)
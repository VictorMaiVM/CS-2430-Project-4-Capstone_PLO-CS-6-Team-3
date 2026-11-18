#Team name:     Team 3
#Team members:  Dominique Frank, Victor Mai, Erich Mundt
#Course:        CS 2430, section 502
#Project:       Programming Project 4

# Represents the single player moving around the board.
class Player:
    # Tracks player position, jail state, consecutive doubles, and cards.
    def __init__(self):
        # Starts at GO (index 0)
        self.position = 0
        self.in_jail = False
        self.jail_turns = 0
        self.consecutive_doubles = 0
        # Count of held Get Out of Jail Free cards
        self.jail_free_cards = 0
#Team name:     Team 3
#Team members:  Dominique Frank, Victor Mai, Erich Mundt
#Course:        CS 2430, section 502
#Project:       Programming Project 4

import random
from board import initialize_board
from deck import Deck
from player import Player

# Simulation engine managing board squares, cards, dice, and turn execution.
class MonopolySimulation:

    def __init__(self, jail_strategy="A"):
        self.jail_strategy = jail_strategy
        self.board = initialize_board()

        self.chance_deck = Deck([
            "Advance to Boardwalk",
            "Advance to Go (Collect $200)",
            "Advance to Illinois Avenue. If you pass Go, collect $200",
            "Advance to St. Charles Place. If you pass Go, collect $200",
            "Advance to the nearest Railroad",
            "Advance to the nearest Railroad",
            "Advance token to nearest Utility",
            "Bank pays you dividend of $50",
            "Get Out of Jail Free",
            "Go Back 3 Spaces",
            "Go to Jail. Go directly to Jail, do not pass Go, do not collect $200",
            "Make general repairs on all your property",
            "Speeding fine $15",
            "Take a trip to Reading Railroad. If you pass Go, collect $200",
            "You have been elected Chairman of the Board. Pay each player $50",
            "Your building loan matures. Collect $150"
        ], "Chance")

        self.chest_deck = Deck([
            "Advance to Go (Collect $200)",
            "Bank error in your favor. Collect $200",
            "Doctor’s fee. Pay $50",
            "From sale of stock you get $50",
            "Get Out of Jail Free",
            "Go to Jail. Go directly to jail, do not pass Go, do not collect $200",
            "Holiday fund matures. Receive $100",
            "Income tax refund. Collect $20",
            "It is your birthday. Collect $10 from every player",
            "Life insurance matures. Collect $100",
            "Pay hospital fees of $100",
            "Pay school fees of $50",
            "Receive $25 consultancy fee",
            "You are assessed for street repair",
            "You have won second prize in a beauty contest. Collect $10",
            "You inherit $100"
        ], "CommunityChest")

        self.player = Player()
        self.total_moves = 0

    # Rolls two 6-sided dice. Returns (die1, die2, is_double).
    def roll_dice(self):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        return d1, d2, (d1 == d2)

    # Sends the player directly to Jail (Square 10).
    def send_to_jail(self):
        self.player.position = 10
        self.player.in_jail = True
        self.player.jail_turns = 0
        self.player.consecutive_doubles = 0

    # Handles player turn execution while in jail based on strategy A or B.
    def handle_jail_turn(self):
        if self.player.jail_free_cards > 0:
            self.player.jail_free_cards -= 1
            self.player.in_jail = False
            self.player.jail_turns = 0
            return True

        d1, d2, is_double = self.roll_dice()

        if self.jail_strategy == "A":
            self.player.in_jail = False
            self.player.jail_turns = 0
            self.move_player(d1 + d2)
            return True
        else:
            if is_double:
                self.player.in_jail = False
                self.player.jail_turns = 0
                self.move_player(d1 + d2)
                return True
            else:
                self.player.jail_turns += 1
                if self.player.jail_turns >= 3:
                    self.player.in_jail = False
                    self.player.jail_turns = 0
                    self.move_player(d1 + d2)
                    return True
                return False

    # Moves player forward by specified steps, wrapping around the 40 squares.
    def move_player(self, steps):
        self.player.position = (self.player.position + steps) % 40
        self.apply_square_effect()

    # Applies landing effects for the current square and handles recursive card triggers.
    def apply_square_effect(self):
        sq = self.board[self.player.position]

        if sq.square_type == "GoToJail":
            self.send_to_jail()
            self.board[self.player.position].landing_count += 1
            return

        if sq.square_type == "Chance":
            card = self.chance_deck.draw_card()
            self.execute_chance_card(card)
            return

        if sq.square_type == "CommunityChest":
            card = self.chest_deck.draw_card()
            self.execute_chest_card(card)
            return

        self.board[self.player.position].landing_count += 1

    # Executes the effect of a drawn Chance card.
    def execute_chance_card(self, card):
        if "Advance to Go" in card:
            self.player.position = 0
            self.board[0].landing_count += 1
        elif "Illinois Avenue" in card:
            self.player.position = 24
            self.board[24].landing_count += 1
        elif "St. Charles Place" in card:
            self.player.position = 11
            self.board[11].landing_count += 1
        elif "Reading Railroad" in card:
            self.player.position = 5
            self.board[5].landing_count += 1
        elif "Boardwalk" in card:
            self.player.position = 39
            self.board[39].landing_count += 1
        elif "Go to Jail" in card:
            self.send_to_jail()
            self.board[10].landing_count += 1
        elif "Go Back 3 Spaces" in card:
            self.player.position = (self.player.position - 3) % 40
            self.apply_square_effect()
        elif "Get Out of Jail Free" in card:
            self.player.jail_free_cards += 1
            self.board[self.player.position].landing_count += 1
        elif "nearest Railroad" in card:
            pos = self.player.position
            if pos > 35 or pos < 5:
                self.player.position = 5
            elif 5 <= pos < 15:
                self.player.position = 15
            elif 15 <= pos < 25:
                self.player.position = 25
            else:
                self.player.position = 35
            self.board[self.player.position].landing_count += 1
        elif "nearest Utility" in card:
            pos = self.player.position
            if 12 <= pos < 28:
                self.player.position = 28
            else:
                self.player.position = 12
            self.board[self.player.position].landing_count += 1
        else:
            # Cash-only cards do not move the player; record landing on Chance square
            self.board[self.player.position].landing_count += 1

    # Executes the effect of a drawn Community Chest card.
    def execute_chest_card(self, card):
        if "Advance to Go" in card:
            self.player.position = 0
            self.board[0].landing_count += 1
        elif "Go to Jail" in card:
            self.send_to_jail()
            self.board[10].landing_count += 1
        elif "Get Out of Jail Free" in card:
            self.player.jail_free_cards += 1
            self.board[self.player.position].landing_count += 1
        else:
            # Cash-only cards do not move the player; record landing on Community Chest square
            self.board[self.player.position].landing_count += 1

    # Simulates a single complete player turn.
    def take_turn(self):
        if self.player.in_jail:
            released = self.handle_jail_turn()
            if not released:
                return

        d1, d2, is_double = self.roll_dice()

        if is_double:
            self.player.consecutive_doubles += 1
            if self.player.consecutive_doubles == 3:
                self.send_to_jail()
                return
        else:
            self.player.consecutive_doubles = 0

        self.move_player(d1 + d2)
        self.total_moves += 1

    # Runs simulation up to target_turns.
    def run_simulation(self, target_turns):
        for _ in range(target_turns):
            self.take_turn()

    # Resets board counts and player state for a new batch run.
    def reset_simulation(self):
        for sq in self.board:
            sq.reset_count()
        self.player = Player()
        self.total_moves = 0
        self.chance_deck.reset_deck()
        self.chest_deck.reset_deck()
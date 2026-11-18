#Team name:     Team 3
#Team members:  Dominique Frank, Victor Mai, Erich Mundt
#Course:        CS 2430, section 502
#Project:       Programming Project 4

import random

# Represents Chance or Community Chest decks, shuffling, and discards
class Deck:
    def __init__(self, card_list, name="Deck"):
        self.name = name
        self.initial_cards = card_list
        self.draw_pile = []
        self.discard_pile = []
        self.reset_deck()

    # Resets and shuffles the deck.
    def reset_deck(self):
        self.draw_pile = list(self.initial_cards)
        random.shuffle(self.draw_pile)
        self.discard_pile = []

    # Draws a card. If the draw pile is empty, reshuffles the discard pile.
    def draw_card(self):
        if not self.draw_pile:
            if not self.discard_pile:
                return None
            self.draw_pile = list(self.discard_pile)
            self.discard_pile = []
            random.shuffle(self.draw_pile)

        card = self.draw_pile.pop(0)
        if card != "GET_OUT_OF_JAIL":
            self.discard_pile.append(card)
        return card

    # Returns a Get Out of Jail Free card back to the discard pile.
    def return_jail_card(self):
        self.discard_pile.append("GET_OUT_OF_JAIL")
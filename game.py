import random

SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]


def create_deck():
    deck = []

    for suit in SUITS:
        for value in range(1, 14):
            deck.append((value, suit))

    return deck


def card_name(card):
    value, suit = card

    names = {
        1: "Ace",
        11: "Jack",
        12: "Queen",
        13: "King"
    }

    name = names.get(value, str(value))

    return f"{name} of {suit}"

import random

from game import create_deck, card_name
from agent import choose_prediction


def play_game():

    deck = create_deck()

    random.shuffle(deck)

    current_card = deck.pop()

    score = 0
    rounds = 0

    while len(deck) > 0:

        prediction, p_higher, p_lower = choose_prediction(
            current_card, deck
        )

        next_card = deck.pop()

        rounds += 1

        print("\nCurrent card:", card_name(current_card))

        print("Agent predicts:", prediction)

        print("Probability of higher:", round(p_higher * 100, 2), "%")

        print("Probability of lower:", round(p_lower * 100, 2), "%")

        print("Next card:", card_name(next_card))

        if next_card[0] == current_card[0]:

            print("Tie! No points.")

        elif prediction == "higher" and next_card[0] > current_card[0]:

            print("Correct prediction!")
            score += 1

        elif prediction == "lower" and next_card[0] < current_card[0]:

            print("Correct prediction!")
            score += 1

        else:

            print("Wrong prediction!")

        current_card = next_card

    print("\nGame completed!")

    print("Total rounds:", rounds)
    print("Agent score:", score)


if __name__ == "__main__":
    play_game()

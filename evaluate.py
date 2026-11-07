import random

from game import create_deck
from agent import choose_prediction


def simulate_game(strategy):

    deck = create_deck()
    random.shuffle(deck)

    current_card = deck.pop()

    correct = 0
    decisive = 0

    while deck:

        if strategy == "probability":

            prediction, _, _ = choose_prediction(
                current_card, deck
            )

        else:

            prediction = random.choice(
                ["higher", "lower"]
            )

        next_card = deck.pop()

        if next_card[0] != current_card[0]:

            decisive += 1

            if prediction == "higher" and next_card[0] > current_card[0]:
                correct += 1

            elif prediction == "lower" and next_card[0] < current_card[0]:
                correct += 1

        current_card = next_card

    return correct, decisive


def evaluate():

    games = 1000

    agent_correct = 0
    agent_decisive = 0

    random_correct = 0
    random_decisive = 0

    for _ in range(games):

        correct, decisive = simulate_game("probability")

        agent_correct += correct
        agent_decisive += decisive

        correct, decisive = simulate_game("random")

        random_correct += correct
        random_decisive += decisive

    agent_rate = agent_correct / agent_decisive * 100

    random_rate = random_correct / random_decisive * 100

    print("Games:", games)

    print("Probability agent accuracy:", round(agent_rate, 2), "%")

    print("Random agent accuracy:", round(random_rate, 2), "%")


if __name__ == "__main__":
    evaluate()

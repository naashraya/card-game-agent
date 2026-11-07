import random


def choose_prediction(current_card, remaining_deck):

    current_value = current_card[0]

    higher = 0
    lower = 0

    for card in remaining_deck:

        if card[0] > current_value:
            higher += 1

        elif card[0] < current_value:
            lower += 1

    total = len(remaining_deck)

    p_higher = higher / total
    p_lower = lower / total

    if p_higher > p_lower:
        prediction = "higher"

    elif p_lower > p_higher:
        prediction = "lower"

    else:
        prediction = random.choice(["higher", "lower"])

    return prediction, p_higher, p_lower

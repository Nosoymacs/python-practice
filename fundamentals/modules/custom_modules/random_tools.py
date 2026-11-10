# Module random_tools.py functions

import random

def random_items(items):
    if len(items) < 2:
        raise ValueError("Not enough items")
    return random.sample(items, 2)

def random_scores(players):
    scores = []
    for _ in range(players):
        scores.append(random.randint(1, 100))
    return scores
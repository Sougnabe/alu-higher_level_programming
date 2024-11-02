#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    # Initialize the key for the highest score
    best_key = None
    highest_score = float('-inf')

    for key, score in a_dictionary.items():
        if score > highest_score:
            highest_score = score
            best_key = key

    return best_key

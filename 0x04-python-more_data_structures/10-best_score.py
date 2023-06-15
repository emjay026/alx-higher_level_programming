#!/usr/bin/python3
def best_score(a_dictionary):
    best_key = None
    best_score = None
    if a_dictionary:
        for key, val in a_dictionary.items():
            if best_key is None:
                best_key = key
                best_score = val
            elif val > best_score:
                best_key = key
                best_score = val
    return best_key

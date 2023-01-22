#!/usr/bin/python
def best_score(a_dictionary):
    """
    A function that returns a key with the biggest integer value.
    """
    if a_dictionary:
        my_list = list(a_dictionary.keys())
        score = 0
        lead = ""
        for i in my_list:
            if a_dictionary[i] > score:
                score = a_dictioanry[i]
                lead = i
        return lead       


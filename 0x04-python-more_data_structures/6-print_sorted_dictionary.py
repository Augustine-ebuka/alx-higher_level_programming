#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    function that sorst 
    dicianary by key
    """
    myKeys = list(a_dictionary.keys())
    myKeys.sort()
    sorted_dict = {i: myDict[i] for i in myKeys}
    return(sorted_dict)

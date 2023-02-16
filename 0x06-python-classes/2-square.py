#!/usr/bin/python3

"""defines a class square"""
class Square:
    """Args:
    size(int): istatiate the class
    """
    def __init__(self, size=0):
        if(isinstance(size, int):
                raise TypeError("size must be an integer")
        elif(size < 0):
                raise ValueError("size must be >= 0")

        self.size = size




#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """getter method """
        return(self.__size)
    @size.stter
    def size(self,value):
        """this is the stter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif(value < 0):
            raise ValueError("size must be >= 0")
        self.__size =value 

    def area(self):
        """ return the area of the square """
        return(self.__size * self.__size)

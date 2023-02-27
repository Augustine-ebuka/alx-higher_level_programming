#!/usr/bin/python3
"""this object is about listing and inheritance"""
class MyList(list):
  """list: the list we will sort"""
  def __init__(self):
    super().__init__()
    
  def print_sorted(self):
    """the funstion that print sorted list"""
    print(sorted(self))


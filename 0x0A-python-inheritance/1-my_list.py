#!/usr/bin/python3
"""A list that inherits and prints
    a sorted list
    """

class Mylist(list):
    """class that inherits from list"""

    def print_sorted(self):
        """method that sorts ots list and prints"""

        sorted_list = sorted(self)
        print(sorted_list)

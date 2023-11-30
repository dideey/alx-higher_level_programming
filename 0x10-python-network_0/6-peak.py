#!/usr/bin/python3

def find_peak(list_of_integers):
    """finds the peak"""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
    else:
        return None

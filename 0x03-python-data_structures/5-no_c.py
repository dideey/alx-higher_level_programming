#!/usr/bin/python3
def capital(my_string):
    return my_string.translate({ord('C'): None})


def no_c(my_string):
    return capital(my_string).translate({ord('c'): None})

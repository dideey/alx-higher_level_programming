#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        while x < count:
        print(my_list[count], end="", type(int))
        count += 1
    except (IndexError, TypeError):
        pass
    print()
    return count


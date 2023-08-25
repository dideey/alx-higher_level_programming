#!/usr/bin/python3
def uppercase(str):
    for i in str:
        up = chr(ord(i) - 32) if 97 <= ord(i) <= 122 else i
        print("{}".format(up), end='')
    print()

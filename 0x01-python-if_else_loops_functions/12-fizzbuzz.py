#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100):
        if not(i % 3) and not (i % 5):
            print("FizzBuzz", end=" ")
            continue
        if not (i % 5):
            print("Buzz", end=" ")
            continue
        if not(i % 3):
            print("Fizz", end=" ")
            continue
        print(i, end=" ")
    else:
        i += 1
        if not(i % 3) and not (i % 5):
            print("FizzBuzz", end=' ')
        if not (i % 5):
            print("Buzz", end=' ')
        if not(i % 3):
            print("Fizz", end=' ')

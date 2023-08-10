#!/usr/bin/python3
if __name__ == "__main__":
from calculator_1 import add, sub, mul, div
#defination
a = 10
b = 5
#output
result1 = add(a, b)
result2 = sub(a, b)
result3 = mul(a, b)
result4 = div(a, b)
#printing
print("{} + {} = {}".format(a, b, result1))
print("{} - {} = {}".format(a, b, result2))
print("{} * {} = {}".format(a, b, result3))
print("{} / {} = {}".format(a, b, result4))

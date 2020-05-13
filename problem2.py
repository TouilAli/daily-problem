""" This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was[1, 2, 3, 4, 5], the expected output would be[120, 60, 40, 30, 24]. If our input was[3, 2, 1], the expected output would be[2, 3, 6].

Follow-up: what if you can't use division?
"""

import timeit

numbers = [1, 2, 3, 4, 5]
output = []

# Solution 1
def f1(
        r:  1):
    l = len(numbers)
    for i in range(0, l):
        output.insert(i, 1)
        for j in range(0, l):
            if (i != j):
                output[i] *= numbers[j]
    return output

# Solution 2 : Using division
def f2():
    l = len(numbers)
    for i in range(0, l):
        output.insert(i, 1)
        for j in range(0, l):
            output[i] *= numbers[j]
        output[i] = int(output[i] / numbers[i])
    return output

# Solution 3
def f3():
    output = []
    right = 1
    for n in reversed(numbers):
        output.insert(0, right)
        right *= n

    left = 1
    for i, n in enumerate(numbers):
        output[i] *= left
        left *= n
    return output

print("S1: ", timeit.timeit(f1, number=10), f1())
print("S2: ", timeit.timeit(f2, number=10), f2())
print("S3: ", timeit.timeit(f3, number=10), f3())

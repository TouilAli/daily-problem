""" This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass ? """

import timeit

print("This line will be printed.")

k = 25
numbers = [10, 15, 3, 7]

# Solution 1


def f1():
    l = len(numbers)
    for i in range(l):
        for j in range(i + 1, l):
            if k == numbers[i] + numbers[j]:
                return True
    return False


# Solution 2
def f2():
    s = set()
    for n in numbers:
        if k - n in s:
            return True
        s.add(n)
    return False

# Solution 3


def f3():
    return bool({k - n for n in numbers} & set(numbers))

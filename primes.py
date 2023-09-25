"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

import math


def is_prime(num: int):
    for divisor in range(2, math.ceil(num / 2) + 1):
        if num % divisor == 0:
            return False
    return True


def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError()
    _list = []
    current_num = 1
    while len(_list) < number_of_primes:
        current_num += 1
        if is_prime(current_num):
            _list.append(current_num)
    return _list

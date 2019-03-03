""" Utility functions """

from functools import reduce

def fibonacci(n):
    assert n > 0
    fib_reduct = reduce(lambda x, n: [x[1],x[0]+x[1]], range(1, n),[0,1])[0]
    return fib_reduct

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n > 2:
        for i in range(2, int((n**0.5)+2)):
            if n%i == 0:
                return False
        else:
            return True

def largest_prime_factor(n):
    if is_prime(n):
        return n
    
    for i in range(int((n**0.5)+1), 1, -1):
        if n%i == 0 and is_prime(i):
            return i

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a*b//gcd(a, b)

def memoize(func):
    """Decorator for memoization"""
    cache = {}
    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return memoized_func
""" Utility functions """

from functools import reduce
from collections import Counter


def fibonacci(n):
    assert n > 0
    fib_reduct = reduce(lambda x, n: [x[1],x[0]+x[1]], range(1, n),[0,1])[0]
    return fib_reduct


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


def get_prime_factorisation(n):
    primes = []
    i = 2
    while i**2 <= n:
        if not n%i:
            n //= i
            primes.append(i)
        else:
            i += 1
    primes.append(n)
    return dict(Counter(primes))


def largest_prime_factor(n):
    return max(get_prime_factorisation(n).keys())


def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


def lcm(a, b):
    return a*b//gcd(a, b)


@memoize
def phi(n):
    """ Euler's Totient Function """
    if n%4 == 0:
        return 2*phi(n//2)
    if (n/2)%2 == 1:
        return phi(n//2)
    y = n
    for i in range(2,n+1):
        if n%i == 0 and is_prime(i):
            y *= 1 - 1.0/i
    return int(y)
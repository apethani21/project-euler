import time
import string
import itertools
from util import is_prime

start_time = time.time()

def n_digit_pandigital_numbers(n):
    perms = itertools.permutations(string.digits[1:n+1][::-1])
    perms = [''.join(perm) for perm in perms]
    perms = list(map(int, perms))
    return perms

for n in range(9, 1, -1):
    pandigital_numbers = n_digit_pandigital_numbers(n)
    odd_pandigital_numbers = list(filter(lambda x: x%2, pandigital_numbers))
    for number in odd_pandigital_numbers:
        if is_prime(number):
            break
    else:
        continue
    break

print(f"The largest n-digit pandigital prime is {number}")

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
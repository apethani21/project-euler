import time
from util import is_prime

start_time = time.time()

quad = lambda n: n**2 + a*n + b
b_range = list(filter(is_prime, range(1, 1000)))
max_triple = (0, 0, 0)

for a in range(-999, 1000):
    for b in b_range:
        n = 0
        while is_prime(quad(n)):
            n += 1
        if n > max_triple[2]:
            max_triple = (a, b, n)

print(f"Product of a and b: {max_triple[0]*max_triple[1]}")

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
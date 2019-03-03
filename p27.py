import time
from util import is_prime

start_time = time.time()

quad = lambda n: n**2 + a*n + b
b_range = list(filter(is_prime, range(1, 1000)))
max = (0, 0, 0)
for a in range(-999, 1000):
    for b in b_range:
        n = 0
        while is_prime(quad(n)):
            n += 1
        if n > max[2]:
            max = (a, b, n)

print("Product of a and b: {}".format(max[0]*max[1]))

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
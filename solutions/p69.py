import time
from util import is_prime

start_time = time.time()

def prime_generator():
    n = 1
    while True:
        n += 1
        if is_prime(n):
            yield n


primes = prime_generator()
prime_products = []
prod = 1
while prod <= 1e6:
    prod *= next(primes)
    if prod <= 1e6:
        prime_products.append(prod)

print(f"The value of n ≤ 1,000,000 for which n/φ(n) is a maximum is {max(prime_products)}")

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
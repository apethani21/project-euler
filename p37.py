import time
from util import is_prime

start_time = time.time()

def is_truncatable_prime(n):
    if str(n)[0] not in ['2', '3', '5', '7'] or str(n)[-1] not in ['2', '3', '5', '7']:
        return False
    if not is_prime(n):
        return False
    n = str(n)
    truncs = [int(n[i:]) for i in range(len(n))] + [int(n[:i+1]) for i in range(len(n))]
    return all([is_prime(k) for k in truncs])

truncatable_primes = set()
n = 10
while len(truncatable_primes) < 11:
    if is_truncatable_prime(n):
        truncatable_primes.add(n)
    n += 1
print(truncatable_primes)
print(sum(truncatable_primes))

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
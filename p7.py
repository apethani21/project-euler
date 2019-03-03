import time
from util import is_prime

start_time = time.time()

def nth_prime(n):
    p = 2
    count = 1
    k = 3
    while count < n:
        if is_prime(k):
            p = k
            count += 1
        k += 2
    return p

print(nth_prime(10001))

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
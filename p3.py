import time
from util import largest_prime_factor

start_time = time.time()

print(largest_prime_factor(600851475143))

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
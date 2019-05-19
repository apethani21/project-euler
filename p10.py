import time
from util import is_prime

start_time = time.time()

print(sum(filter(is_prime, range(2000000))))

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
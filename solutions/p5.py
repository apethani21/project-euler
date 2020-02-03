import time
from functools import reduce
from util import lcm

start_time = time.time()

def lcm_upto_n(n):
    return reduce(lcm, range(1, n+1))

print(lcm_upto_n(20))

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
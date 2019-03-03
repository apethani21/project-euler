import time
from util import is_prime

start_time = time.time()

s = 0
for i in range(2000000):
    if is_prime(i):
        s += i
print(s)

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
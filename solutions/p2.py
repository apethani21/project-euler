import time
from util import fibonacci

start_time = time.time()

total = 0
n = 1
while fibonacci(n) <= 4000000:
    if not fibonacci(n)%2:
        total += fibonacci(n)
    n += 1
print(total)

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
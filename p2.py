import time
from util import fibonacci

start_time = time.time()

sum = 0
n = 1
while fibonacci(n) <= 4000000:
    if fibonacci(n)%2 == 0:
        sum = sum + fibonacci(n)
    n += 1
print(sum)

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
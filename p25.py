import time
from util import fibonacci
import sys

start_time = time.time()

def number_of_digits(n):
    if n%10 == n:
        return 1
    else:
        return number_of_digits((n - (n%10))//10) + 1

sys.setrecursionlimit(10000)
k = 1
while number_of_digits(fibonacci(k)) < 1000:
    k += 1

print(k+1)

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
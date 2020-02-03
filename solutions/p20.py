import time
from util import memoize

start_time = time.time()

def digit_sum(n):
    s = 0
    while n:
        s += n%10
        n //= 10
    return s

@memoize
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
print(digit_sum(factorial(100)))

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
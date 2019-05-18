import time
from util import memoize

start_time = time.time()

@memoize
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def ncr(n, r):
    return factorial(n)/(factorial(r)*factorial(n-r))

counter = 0
for n in range(1, 101):
    for r in range(n//2 + 1):
        if ncr(n, r) > 1000000:
            if n == 2*r:
                counter += 1
            else:
                counter += 2
print(counter)

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
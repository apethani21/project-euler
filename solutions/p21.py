import time
from functools import reduce

start_time = time.time()

def sum_of_divisors(n):
    S = 0
    for i in range(1, n):
        if n%i == 0:
            S += i 
    return S
 
def amicable(a, b):
    if sum_of_divisors(a) == b: 
        if sum_of_divisors(b) == a:
            return True
    else:
        return False
    
amicable_numbers = set()
for x in range(1, 1000):
    for y in range(x+1, 1000):
        if amicable(x, y):
            amicable_numbers.add(x)
            amicable_numbers.add(y)

print(reduce((lambda x, y: x + y), amicable_numbers))

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
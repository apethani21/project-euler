import time
from functools import reduce

start_time = time.time()

def sum_of_divisors(n):
    divs = set()
    i = 1
    while i*i <= n:
        if not n%i:
            divs.update({i, n//i})
        i += 1
    return sum(divs) - n
 
def amicable(a, b):
    return (sum_of_divisors(a) == b) and (sum_of_divisors(b) == a)
    
amicable_numbers = set()
for x in range(1, 1000):
    for y in range(x+1, 1000):
        if amicable(x, y):
            amicable_numbers.update({x, y})

print(reduce((lambda x, y: x + y), amicable_numbers))

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
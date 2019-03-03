import time
from functools import reduce

start_time = time.time()

def sum_of_squares(n):
    return reduce((lambda x, y: x + y), [i**2 for i in range(n+1)])

def square_of_sum(n):
    return reduce((lambda x, y: x + y), range(n+1))**2

print(square_of_sum(100) - sum_of_squares(100))

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
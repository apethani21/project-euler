import time
from util import memoize

start_time = time.time()

@memoize
def a(i, j):
    if (i == 1) or (j == 1):
        return 1
    else:
        return a(i-1, j) + a(i, j-1)

print(a(21, 21))

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
import time
import numpy as np
from util import memoize

start_time = time.time()

@memoize
def collatz(n):
    if n == 1:
        return 1
    elif n%2 == 0:
        return 1 + collatz(n/2)
    else:
        return 1 + collatz(3*n + 1)

L = np.array([collatz(n) for n in range(1, 1000000)])
print('The longest collatz sequence is of length {} for value {}'.format(np.max(L), np.argmax(L)))

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
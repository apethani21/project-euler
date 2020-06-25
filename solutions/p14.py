import time
import numpy as np
from util import memoize

start_time = time.time()

@memoize
def collatz(n):
    if n == 1:
        return 1
    elif not n%2:
        return 1 + collatz(n/2)
    else:
        return 1 + collatz(3*n + 1)

collatz_numbers = np.array([collatz(n) for n in range(1, 1000000)])
print(f"The longest collatz sequence is of length {np.max(collatz_numbers)} for values {np.argmax(collatz_numbers)}")
end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
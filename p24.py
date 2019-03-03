import time
from itertools import permutations
from functools import reduce

start_time = time.time()

def lexilist(n):
    digits = list(map(lambda x: str(x), list(range(n+1))))
    string = reduce(lambda x, y: x+y, list(map(lambda x: str(x), list(range(n+1)))))
    perms = [''.join(p) for p in permutations(string)]
    return perms

print(lexilist(9)[1000000])

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
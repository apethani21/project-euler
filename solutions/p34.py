import time

start_time = time.time()

factorial_lookup = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 7:5040, 8:40320, 9:362880}

def is_curious(n):
    digits = [int(k) for k in list(str(n))]
    return n == sum([factorial_lookup[digit] for digit in digits])

total = 0
for n in range(3, 2000000):
    if is_curious(n):
        total += n

print(total)

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
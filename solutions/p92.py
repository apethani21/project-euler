import time

start_time = time.time()

def squaresum(n):
    total = 0
    while n:
        total += (n % 10)**2
        n //= 10
    return total

def sequence(n):
    seq = [n]
    while squaresum(seq[-1]) not in seq:
        seq.append(squaresum(seq[-1]))
    seq.append(squaresum(seq[-1]))    
    return seq

start_time = time.time()

count = 0
for i in range(1, 10000001):
    if 89 in sequence(i):
        count += 1
print(count)

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
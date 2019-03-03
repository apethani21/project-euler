import time

start_time = time.time()

def squaresum(n):
    total = 0
    while n:
        total += (n % 10)**2
        n //= 10
    return total

def seq(n):
    L = []
    L.append(n)
    while squaresum(L[-1]) not in L:
        L.append(squaresum(L[-1]))
    L.append(squaresum(L[-1]))    
    return L

start_time = time.time()

count = 0
for i in range(1, 10000001):
    if 89 in seq(i):
        count += 1
print(count)

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
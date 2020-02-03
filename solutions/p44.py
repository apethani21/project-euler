import time

start_time = time.time()

p = lambda n: n*(3*n - 1)//2
def is_pent(n):
    s = (((24*n + 1)**0.5)+1)/float(6)
    return int(s) - s == 0

n = 1
j = 1
while n:
    for i in range(1, j+1):
        if is_pent(p(i)+p(j)) and is_pent(p(j)-p(i)):
            print((i, j))
            print((p(i), p(j)))
            print(p(j) - p(i))
            n = 0
            break
    j += 1

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
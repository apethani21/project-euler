import time

start_time = time.time()

d = 1
for i in range(1, 10):
    for j in range(1, i):
        q, r = divmod(9*j*i, 10*j-i)
        if not r and q <= 9:
            d *= i/float(j)

print(d)

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
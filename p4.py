import time

start_time = time.time()

k = 0
for a in range(999, 99, -1):
    for b in range(a, 99, -1):
        x = a*b
        if x > k:
            s = str(a*b)
            if s == s[::-1]:
                k = a*b
print(k)

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
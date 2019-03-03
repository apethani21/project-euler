import time

start_time = time.time()

sum = 0
for i in range(1, 1000):
    if (i%3 == 0) or (i%5 == 0):
        sum = sum + i
print(sum)

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
import time

start_time = time.time()

print(sum([i for i in range(1, 1000) if (i%3 == 0) or (i%5 == 0)]))

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
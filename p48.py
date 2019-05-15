import time

start_time = time.time()

print(sum([n**n for n in range(1, 1001)])%10**10)

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
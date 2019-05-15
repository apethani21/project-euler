import time

start_time = time.time()

print(len({a**b for a in range(2, 101) for b in range(2, 101)}))

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
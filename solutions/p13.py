import time

start_time = time.time()

total = 0
with open('problem13.txt', 'r') as f:
    for line in f:
        total += int(line)
print(str(total)[:10])

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
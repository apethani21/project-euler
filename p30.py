import time

start_time = time.time()

powers = []

for i in range(2,354294):
        total = 0
        for j in str(i):
                total += int(j) ** 5

        if total == i:
                powers.append(i)

print(sum(powers))

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
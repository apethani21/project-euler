import time

start_time = time.time()

powers = []

for i in range(2,354294):
        sum = 0
        for j in str(i):
                sum += int(j) ** 5

        if sum == i:
                powers.append(i)

print(sum(powers))

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
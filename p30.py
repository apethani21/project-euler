import time

start_time = time.time()

powers = []
total = 0

for i in range(2,354294):
        sum = 0
        for j in str(i):
                sum += int(j) ** 5

        if sum == i:
                powers.append(i)

for i in powers:
        total += i

print(total)

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
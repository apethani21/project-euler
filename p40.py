import time

start_time = time.time()

i = 1
champer = ''
while len(champer) < 1000000:
    champer += str(i)
    i += 1

prod = 1
for i in range(0, 7):
    prod *= int(champer[10**i - 1])

print(prod)

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
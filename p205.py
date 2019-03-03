import time
import random

start_time = time.time()

P = 0
C = 0
draw = 0
for i in range(100000):
    peter = random.randint(1,4)
    colin = random.randint(1, 6)
    if peter > colin:
        P += 1
    elif peter < colin:
        C += 1
    else:
        draw += 1

print((P/100000, C/100000, draw/100000))

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
import time
from collections import Counter

start_time = time.time()

perimeters = []
for a in range(1, 500):
    for b in range(a, 500):
        c = (a**2 + b**2)**0.5
        if int(c) == c and a + b + c <= 1000:
            perimeters.append(a+b+c)
p = Counter(perimeters)

print(p.most_common(5))

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
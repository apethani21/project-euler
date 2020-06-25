import time

start_time = time.time()

def is_pythag_triple(a, b, c):
    return a**2 + b**2 == c**2

for a in range(500):
    for b in range(a, 500):
        if is_pythag_triple(a, b, 1000-a-b):
            print(a*b*(1000-a-b))

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
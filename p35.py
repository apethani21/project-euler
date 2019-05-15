import time
from util import is_prime

start_time = time.time()

def generate_rotation(n):
    n = str(n)
    rotations = len(n)
    while rotations > 0:
        yield n
        n = str(n)[-1] + str(n)[:-1]
        rotations -= 1

def is_circular_prime(n):
    if not is_prime(n):
        return False
    digits = list(str(n))
    checklist = ['0', '4', '6', '8']
    if any([d in checklist for d in digits]):
        return False
    cycles = generate_rotation(n)
    while True:
        try:
            if not is_prime(int(next(cycles))):
                return False
        except StopIteration:
            return True

counter = 0
for n in range(1, 1000000):
    if is_circular_prime(n):
        counter += 1
print(counter)

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
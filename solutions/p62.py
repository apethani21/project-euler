import time
from itertools import permutations

start_time = time.time()


def is_cube(n):
    x = n**(1/3)
    return round(x)**3 == n


def integer_permutations(n):
    return {int(''.join(digits))
            for digits in permutations(str(n))
            if digits[0] != "0"}

cubes = {}
n = 4
value_found = False
required_key = None
required_digit_count = None
while not value_found:
    n += 1
    key = ''.join(sorted(str(n**3)))
    cubes.setdefault(key, 0)
    cubes[key] += 1
    if cubes[key] == 5:
        required_key = key
        required_digit_count = len(str(n))
    if required_digit_count is not None and required_digit_count < len(str(n)) and cubes[required_key] == 5:
        value_found = True
print(f"Value found - required key = {required_key}")
perms = sorted(integer_permutations(required_key))
required_cubes = [perm for perm in perms if is_cube(perm)]

print(f"Cubes: {required_cubes}")

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
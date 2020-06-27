import time
import itertools

start_time = time.time()


def zero_to_nine_pandigital_numbers():
    perms = itertools.permutations("0123456789")
    perms = [''.join(perm) for perm in perms]
    perms = list(map(int, perms))
    return perms


def has_divisibility_property(n):
    str_n = str(n)
    sub_ints = [int(str_n[i:i+3]) for i in range(1, 8)]
    div_vals = [2, 3, 5, 7, 11, 13, 17]
    return all([(not sub_int%val) for sub_int, val in zip(sub_ints, div_vals)])


zero_to_nine_pandigitals = zero_to_nine_pandigital_numbers()
total = sum([n for n in zero_to_nine_pandigitals if has_divisibility_property(n)])
print(f"The sum of all 0 to 9 pandigital numbers with this property is {total}")

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
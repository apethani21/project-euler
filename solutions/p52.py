import time

start_time = time.time()

def is_permuted_multiple(n):
    digits = sorted(str(n))
    multiples = [i*n for i in range(2, 7)]
    multiples_counters = [sorted(str(k)) for k in multiples]
    return all([digits == permuted_counter for permuted_counter in multiples_counters])

i = 1
while True:
    if is_permuted_multiple(i):
        print(i)
        break
    i += 1

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
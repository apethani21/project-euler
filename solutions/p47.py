import time
from util import get_prime_factorisation

start_time = time.time()

prime_factorisation_cache = {}

result_found = False
i = 2
while not result_found:
    current_factorisations = {}
    for k in (i, i+1, i+2, i+3):
        if k not in prime_factorisation_cache:
            factorisation = get_prime_factorisation(k)
            prime_factorisation_cache[k] = factorisation
        current_factorisations[k] = prime_factorisation_cache[k]

    prime_factors_count_conditions = {
        k: len(set(factorisation.keys())) >= 4
        for k, factorisation in current_factorisations.items()
    }

    if all(prime_factors_count_conditions.values()):
        result_found = True
    else:
        i += 1

print(f"The first of the four consecutive integers to have four distinct prime factors each is {i}")
print(f"The prime factorisations are: {current_factorisations}")

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
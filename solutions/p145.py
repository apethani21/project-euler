import time

start_time = time.time()


def memoize_all_digits_odd(func):
    cache = dict()
    def memoized_func(n):
        if n in cache:
            return cache[n]
        reverse_n = reverse(n)
        if reverse_n in cache:
            return cache[reverse_n]
        result = func(n)
        cache[n] = result
        cache[int(str(n)[::-1])] = result
        return result

    return memoized_func


def memoize_is_reversible(func):
    cache = dict()
    def memoized_func(n):
        if str(n)[-1] == "0":
            cache[n] = False
        if n in cache:
            return cache[n]
        reverse_n = reverse(n)
        if reverse_n in cache:
            return cache[reverse_n]
        result = func(n)
        cache[n] = result
        cache[int(str(n)[::-1])] = result
        return result

    return memoized_func


is_odd = {str(i): bool(i%2) for i in range(10)}


@memoize_all_digits_odd
def all_digits_odd(n):
    return all([is_odd[digit] for digit in set(str(n))])


@memoize_is_reversible
def is_reversible(n):
    return ((n%10) and (all_digits_odd(n + int(str(n)[::-1]))))


total_reversible = sum([is_reversible(n) for n in range(11, int(1e9))])
print(f"Total reversible numbers = {total_reversible}")

end_time = time.time()
print("Time taken: {} s".format(round((end_time - start_time), 3)))
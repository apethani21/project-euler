import time

start_time = time.time()

def sum_of_divisors(n):
    divs = set()
    i = 1
    while i*i <= n:
        if not n%i:
            divs.update({i, n//i})
        i += 1
    return sum(divs) - n

def is_perfect(n):
    return sum_of_divisors(n) == n

def is_deficient(n):
    return sum_of_divisors(n) < n

def is_abundant(n):
    return sum_of_divisors(n) > n

abundant_numbers = set()
for i in range(1, 28124):
    if is_abundant(i):
        abundant_numbers.add(i)

def is_abundant_sum(n):
    for i in abundant_numbers:
        if i > n:
            return False
        if (n - i) in abundant_numbers:
            return True
    return False

print(sum(x for x in range(1, 28124) if not is_abundant_sum(x)))

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
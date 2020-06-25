import time

start_time = time.time()

def triangular(n):
    return n*(n+1)//2

def num_of_divisors(n):
    divs = 0
    sqrt_n = int(n**0.5)

    for i in range(1, sqrt_n + 1):
        if not n%i:
            divs += 1

    divs *= 2
    if sqrt_n**2 == n:
        divs -= 1
    return divs

x = 0
n = 1
while x < 500:
    x = num_of_divisors(triangular(n))
    n += 1

print(f"Required triangular number = {triangular(n-1)}")
print(f"Number of divisors = {x}")

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
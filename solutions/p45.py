import time

start_time = time.time()


def is_pentagonal(t):
    x = (1/6)*(1 + (1 + 24*t)**0.5)
    return x == int(x)


def is_hexagonal(t):
    x = (1/4)*(1 + (1 + 8*t)**0.5)
    return x == int(x)
    

def triangle(n):
    return int(n*(n+1)/2)


value_found = False
n = 286

while not value_found:
    t = triangle(n)
    if is_hexagonal(t) and is_pentagonal(t):
        value_found = True
    else:
        n += 1

print(f"The next triangle number that is also pentagonal and hexagonal is {t}")



end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
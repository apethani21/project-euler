import time

start_time = time.time()

def is_increasing(n):
    n = str(n)
    return all(n[i+1] >= n[i] for i in range(len(n)-1))

def is_decreasing(n):
    n = str(n)
    return all(n[i+1] <= n[i] for i in range(len(n)-1))

def is_bouncy(n):
    return not(is_decreasing(n) or is_increasing(n))

total = 99
number_of_bouncies = 0
ratio = number_of_bouncies/total

while ratio < 0.99:
    if is_bouncy(total+1):
        number_of_bouncies += 1
    total += 1
    ratio = number_of_bouncies/total

print(total)

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
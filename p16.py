import time

start_time = time.time()

def digit_sum(n):
    s = 0
    while n:
        s += n%10
        n //= 10
    return s

print(digit_sum(2**1000))

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
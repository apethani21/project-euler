import time

start_time = time.time()

def digit_sum(n):
    s = 0
    while n:
        s += n%10
        n //= 10
    return s

max_digit_sum = 0
for a in range(2, 100):
    for b in range(2, 100):
        dig_sum = digit_sum(a**b)
        if dig_sum > max_digit_sum:
            max_digit_sum = dig_sum
            max_a = a
            max_b = b

print("Digit sum of {}^{} equals {}".format(a, b, max_digit_sum))

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
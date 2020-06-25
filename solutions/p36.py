import time

start_time = time.time()

def binary(n):
    return int(bin(n)[2:])

def is_palindrome(n):
    n = str(n)
    return n == n[::-1]

total = 0
for i in range(1, 1000000):
    if is_palindrome(i):
        if is_palindrome(binary(i)):
            total += i
print(total)

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
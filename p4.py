import time

start_time = time.time()

max_palindrome = 0
for a in range(999, 99, -1):
    for b in range(a, 99, -1):
        if a*b > max_palindrome:
            if str(a*b) == str(a*b)[::-1]:
                max_palindrome = a*b
print(max_palindrome)

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
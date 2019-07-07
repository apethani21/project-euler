import time

start_time = time.time()

def has_pandigital_product(n):
	for i in range(1, int(n**0.5) + 1):
		if n%i == 0:
			temp = str(n) + str(i) + str(n // i)
			if "".join(sorted(temp)) == "123456789":
				return True
	return False

total = sum(i for i in range(1, 10000) if has_pandigital_product(i))
print(total)

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
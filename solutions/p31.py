import time

start_time = time.time()

total = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
combinations = [1] + [0]*total

for coin in coins:
    for i in range(coin, total+1):
        combinations[i] += combinations[i - coin]

print(combinations[total])

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
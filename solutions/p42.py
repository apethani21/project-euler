import time

start_time = time.time()

string = ''
with open('p042_words.txt', 'r') as f:
    for line in f:
        string += line
words = [word[1:-1] for word in string.split(',')]
s = '_ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def val(word):
    return sum([s.index(char) for char in word])

triangle = {n*(n+1)//2 for n in range(1, 1000)}

counter = 0
for word in words:
    if val(word) in triangle:
        counter += 1

print(counter)

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
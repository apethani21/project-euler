import time

start_time = time.time()

names = []
with open('p22_names.txt', 'r') as f:
    for line in f:
        l = line.split(',')
        for name in l:
            names.append(name[1:-1])
            
names.sort()

def val(name):
    chars = '_ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return sum([chars.index(i) for i in name])

def rank(name):
    return names.index(name) + 1

total = 0
for name in names:
    total += val(name)*rank(name)

print(total)

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
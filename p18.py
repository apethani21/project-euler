import time

start_time = time.time()

with open('triangle.txt', 'r') as f:
    triangle = [[int(i) for i in line.split()] for line in f]
    
for x in reversed(range(len(triangle))):
    for y in range(x):
        triangle[x-1][y]+=max(triangle[x][y],triangle[x][y+1])
        
print(triangle[0][0])

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
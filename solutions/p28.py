import time

start_time = time.time()

"""
For an n x n grid:
top_right(n) = n^2
top_left(n) = n^2 - (n - 1)
bottom_left(n) = n^2 - 2*(n - 1)
bottom_right(n) = n^2 - 3*(n - 1)
Want the sum of each of these four corners for odd integers beteen 3 and 1001, with 1 added for the centre.
"""

print(1 + sum([16*(n**2) + 4*n + 4 for n in range(1, 501)]))

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
import time
from functools import reduce
import inflect

start_time = time.time()

print(reduce((lambda x, y: x+y), [len(p.number_to_words(i).replace("-", "").replace(" ", "")) for i in range(1, 1001)]))

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
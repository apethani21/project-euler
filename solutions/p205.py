import time
import numpy as np

start_time = time.time()

samples = 1e7
peter_scores = np.random.randint(1, 5, int(samples))
colin_scores = np.random.randint(1, 7, int(samples))
peter_wins = (peter_scores > colin_scores).sum()
colin_wins = (peter_scores < colin_scores).sum()
draws = (peter_scores == colin_scores).sum()

print((peter_wins/samples), (colin_wins/samples), (draws/samples))

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
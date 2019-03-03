import time
from datetime import date

start_time = time.time()

sundays = 0
for year in range(1901,2001):
    for month in range(1,13):
        if date(year,month,1).weekday() == 6:
            sundays+=1
print(sundays)

end_time = time.time()

print("Time taken: {} ms".format(round((end_time - start_time)*1000, 3)))
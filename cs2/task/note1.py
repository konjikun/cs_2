import  time
time_sta = time.time()
import random
target = sorted(random.sample(range(100000), k=10))
print(target)
time_end = time.time()
print(time_end-time_sta)
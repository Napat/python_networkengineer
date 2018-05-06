import numpy as np
import time

numMin = []     # min value series
numMax = []     # max value series
numAvg = []     # average series
ts = []         # timesec series

tformat = "%d/%m/%Y"
print(time.strftime(tformat))
tformat = "%H:%M"
#tformat = "%H:%M:%S"
for i in range(5):
   numMin.append(np.random.randint(1, high=3))
   numMax.append(np.random.randint(10, high=15))
   numAvg.append(np.random.randint(3, high=10))
   ts.append(time.strftime(tformat))
   print("!", end='', flush=True)     # no new line and force flush to output
   time.sleep(1)    # time.sleep(60)
print('')
for i in range(5):
   print(ts[i],"Min:",numMin[i],"Max:",numMax[i],"Average:",numAvg[i])

""" Output
06/05/2018
!!!!!
11:37 Min: 2 Max: 11 Average: 5
11:37 Min: 2 Max: 11 Average: 9
11:37 Min: 1 Max: 13 Average: 9
11:37 Min: 1 Max: 12 Average: 5
11:37 Min: 1 Max: 12 Average: 4
"""

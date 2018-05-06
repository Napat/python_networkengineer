import pandas as pd
import numpy as np
import time

numMin = []
numMax = []
numAvg = []
# Time series 11.00, 11:05, 11:10, 11:15, 11:20
ts = pd.date_range("11:00", "11:20", freq="5min")
print("------")
print(ts)

for i in range(5):
   numMin.append(np.random.randint(1,high=3))
   numMax.append(np.random.randint(10,high=15))
   numAvg.append(np.random.randint(3,high=10))

df = pd.DataFrame({'time': ts, 'min': numMin, 'max': numMax, 'avg': numAvg})
print("------")
print(df)
print("------")
print(df.shape)
print("------")
print(df['avg'])
print("------")
print(df['avg'].min())
print("------")
print(df['avg'].max())
print("------")
print(df[(df['time'] > '2018-05-05 11:05:00')])


""" Output
------
DatetimeIndex(['2018-05-06 11:00:00', '2018-05-06 11:05:00',
               '2018-05-06 11:10:00', '2018-05-06 11:15:00',
               '2018-05-06 11:20:00'],
              dtype='datetime64[ns]', freq='5T')
------
   avg  max  min                time
0    3   11    1 2018-05-06 11:00:00
1    8   13    2 2018-05-06 11:05:00
2    4   10    2 2018-05-06 11:10:00
3    6   14    2 2018-05-06 11:15:00
4    5   14    2 2018-05-06 11:20:00
------
(5, 4)
------
0    3
1    8
2    4
3    6
4    5
Name: avg, dtype: int64
------
3
------
8
------
   avg  max  min                time
0    3   11    1 2018-05-06 11:00:00
1    8   13    2 2018-05-06 11:05:00
2    4   10    2 2018-05-06 11:10:00
3    6   14    2 2018-05-06 11:15:00
4    5   14    2 2018-05-06 11:20:00
"""

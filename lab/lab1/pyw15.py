import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure("Network Connection Test")
tformat = "%d/%m/%Y"
timeStartDay = time.strftime(tformat)
tformat = "%H:%M:%S"

numMin = []
numMax = []
numAvg = []
ts = []
df = []

def animate(i):   
   numMin.append(np.random.randint(0,high=3))
   numMax.append(np.random.randint(10,high=15))
   numAvg.append(np.random.randint(3,high=10))
   ts.append(time.strftime(tformat))
   df = pd.DataFrame({'time': ts, 'min': numMin, 'max': numMax, 'avg': numAvg})
   fig.clear()
   plt.plot( 'time', 'avg', data=df, marker='o', markerfacecolor='blue', markersize=6, color='skyblue', linewidth=4)
   plt.plot( 'time', 'min', data=df, marker='x', color='green', linewidth=2)
   plt.plot( 'time', 'max', data=df, marker='', color='red', linewidth=2)
   plt.legend()
   plt.ylabel('RTT (ms)')
   plt.xlabel(timeStartDay)	
   
   print("-----")
   print("numMin: ", numMin)
   print("numMax: ", numMax)
   print("numAvg: ", numAvg)
   print("ts: ", ts)
   print("df: ", df)

# Makes an animation by repeatedly calling a animate function
ani = animation.FuncAnimation(fig, animate, interval=10000)
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import subprocess
import re

welcome = """
888b     d888 888b    888 8888888b.  
8888b   d8888 8888b   888 888   Y88b 
88888b.d88888 88888b  888 888    888 
888Y88888P888 888Y88b 888 888   d88P 
888 Y888P 888 888 Y88b888 8888888P"  
888  Y8P  888 888  Y88888 888 T88b   
888   "   888 888   Y8888 888  T88b  
888       888 888    Y888 888   T88b 
------------------------------------------------------------------------------------------
MAHANAKORN Network Research Laboratory
------------------------------------------------------------------------------------------
                                 _   _       _ _           _            _   _             
  ___ ___  _ __  _ __   ___  ___| |_(_)_   _(_) |_ _   _  | |_ ___  ___| |_(_)_ __   __ _ 
 / __/ _ \| '_ \| '_ \ / _ \/ __| __| \ \ / / | __| | | | | __/ _ \/ __| __| | '_ \ / _` |
| (_| (_) | | | | | | |  __/ (__| |_| |\ V /| | |_| |_| | | ||  __/\__ \ |_| | | | | (_| |
 \___\___/|_| |_|_| |_|\___|\___|\__|_| \_/ |_|\__|\__, |  \__\___||___/\__|_|_| |_|\__, |
                                                   |___/                            |___/ 
"""
print(welcome)

fig = plt.figure("Network Connection Test")
tformat = "%d/%m/%Y"
timeStartDay = time.strftime(tformat)
tformat = "%H:%M"

# IP traget
traget = "1.1.1.1"
pattern = re.compile(r'\d+')

numMin = []
numMax = []
numAvg = []
ts = []
df = []

def animate(i):
   #initial values; assume timeout
   result = subprocess.run(["ping",traget], stdout=subprocess.PIPE, universal_newlines="\r\n")
   if result.returncode == 0:
      rtt = result.stdout[result.stdout.find('Minimum'):]
      arr = pattern.findall(rtt)
      numMin.append(int(arr[0]))
      numMax.append(int(arr[1]))
      numAvg.append(int(arr[2]))
      print('!',end='' ,flush=True)
   else:
      numMin.append(-1)
      numMax.append(-1)
      numAvg.append(-1)
      print('.',end='' ,flush=True)
   
   ts.append(time.strftime(tformat))
   df = pd.DataFrame({'time': ts, 'min': numMin, 'max': numMax, 'avg': numAvg})
   fig.clear()
   plt.plot( 'time', 'avg', data=df, marker='o', markerfacecolor='blue', markersize=6, color='skyblue', linewidth=4)
   plt.plot( 'time', 'min', data=df, marker='', color='green', linewidth=2)
   plt.plot( 'time', 'max', data=df, marker='', color='red', linewidth=2)
   plt.legend()
   plt.ylabel('RTT (ms)')
   plt.xlabel(timeStartDay)	
   
ani = animation.FuncAnimation(fig, animate, interval=60000)
plt.show()


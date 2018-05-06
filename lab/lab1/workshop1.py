import subprocess
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

ascii_art_text01 = """
                                                    
RRRRRRRRRRRRRRRRR                                     
R::::::::::::::::R                                    
R::::::RRRRRR:::::R                                   
RR:::::R     R:::::R                                  
  R::::R     R:::::R   ooooooooooo      ooooooooooo   
  R::::R     R:::::R oo:::::::::::oo  oo:::::::::::oo 
  R::::RRRRRR:::::R o:::::::::::::::oo:::::::::::::::o
  R:::::::::::::RR  o:::::ooooo:::::oo:::::ooooo:::::o
  R::::RRRRRR:::::R o::::o     o::::oo::::o     o::::o
  R::::R     R:::::Ro::::o     o::::oo::::o     o::::o
  R::::R     R:::::Ro::::o     o::::oo::::o     o::::o
  R::::R     R:::::Ro::::o     o::::oo::::o     o::::o
RR:::::R     R:::::Ro:::::ooooo:::::oo:::::ooooo:::::o
R::::::R     R:::::Ro:::::::::::::::oo:::::::::::::::o
R::::::R     R:::::R oo:::::::::::oo  oo:::::::::::oo 
RRRRRRRR     RRRRRRR   ooooooooooo      ooooooooooo   
                                                                                                          
"""

ip_addr = "1.1.1.1"
fig = plt.figure("Network Connection Test")
tformat = "%d/%m/%Y"
timeStartDay = time.strftime(tformat)
tformat = "%H:%M:%S"

numMin = []
numMax = []
numAvg = []
ts = []
df = []

def myping(ipaddr):
    # Windows
    result = subprocess.run(["ping", ipaddr], stdout=subprocess.PIPE, universal_newlines="\r\n")
    #Linux
    #result = subprocess.run(["ping", ipaddr, "-c", "4"], stdout=subprocess.PIPE, universal_newlines="\r\n")
    
    #print("return code:", result.returncode)
    # print(result.stdout)
    if result.returncode == 0:  # ping ok
        return True, result.stdout     # isping, output string
    
    return False, ""

def getminmaxavg(line_minmaxavg):
    pattern = re.compile(r'\d+')            # Windows
    #pattern = re.compile(r'\d+.\d+')       # Linux
    result = pattern.findall(line_minmaxavg)
    #print(result)
    # print("Min:", result[0])
    # print("Max:", result[1])
    # print("Average:", result[2])
    return result[0], result[1], result[2]  # min, max, average

def pingpoint(ip_addr):
    isping, pingstring = myping(ip_addr)
    # print(isping)
    # print(pingstring)

    if isping == True:
        line_minmaxavg = pingstring[pingstring.find('Minimum'):]
        pmin, pmax, pavg = getminmaxavg(line_minmaxavg)
        # print(pmin, pmax, pavg)
        print("!", end='', flush=True)
        return pmin, pmax, pavg
    else:
        print(".", end='', flush=True)
        return -1, -1, -1

def animate(i):
    pmin, pmax, pavg = pingpoint(ip_addr)

    numMin.append(int(pmin))
    numMax.append(int(pmax))
    numAvg.append(int(pavg))
    ts.append(time.strftime(tformat))
    df = pd.DataFrame({'time': ts, 'min': numMin, 'max': numMax, 'avg': numAvg})
    fig.clear()
    plt.plot('time', 'avg', data=df, marker='o', markerfacecolor='blue',
            markersize=6, color='skyblue', linewidth=4)
    plt.plot('time', 'min', data=df, marker='x', color='green', linewidth=2)
    plt.plot('time', 'max', data=df, marker='', color='red', linewidth=2)
    plt.legend()
    plt.ylabel('RTT (ms)')
    plt.xlabel(timeStartDay)


print(ascii_art_text01)
ani = animation.FuncAnimation(fig, animate, interval=10000)
plt.show()

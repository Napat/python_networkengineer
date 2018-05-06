import re
import time

pingResult = """\n
Pinging 1.1.1.1 with 32 bytes of data:
Reply from 1.1.1.1: bytes=32 time=32ms TTL=54
Reply from 1.1.1.1: bytes=32 time=31ms TTL=54
Reply from 1.1.1.1: bytes=32 time=32ms TTL=54
Reply from 1.1.1.1: bytes=32 time=32ms TTL=54

Ping statistics for 1.1.1.1:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 34.10ms, Maximum = 63.02ms, Average = 41.85ms
"""

print("-----")
print(pingResult)

lineInterest = pingResult[pingResult.find('Minimum'):]

print("-----")
print(lineInterest)

print("-----")
pattern = re.compile(r'\d+.\d+')
result = pattern.findall(lineInterest)
print(result)
print("Min:",result[0])
print("Max:",result[1])
print("Average:",result[2])

print("----- time module")
tformat = "%d/%m/%Y"    # date/month/year i.e.: 06/05/2018
timeStartDay = time.strftime(tformat)
print(timeStartDay)

time.sleep(2)   # delay 2 seconds

tformat = "%H:%M:%S"   # hour:minute:sec i.e: 11:20:52
timeNow = time.strftime(tformat)
print(timeNow)

""" Output
-----

Pinging 1.1.1.1 with 32 bytes of data:
Reply from 1.1.1.1: bytes=32 time=32ms TTL=54
Reply from 1.1.1.1: bytes=32 time=31ms TTL=54
Reply from 1.1.1.1: bytes=32 time=32ms TTL=54
Reply from 1.1.1.1: bytes=32 time=32ms TTL=54

Ping statistics for 1.1.1.1:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 34.10ms, Maximum = 63.02ms, Average = 41.85ms

-----
Minimum = 34.10ms, Maximum = 63.02ms, Average = 41.85ms

-----
['34.10', '63.02', '41.85']
Min: 34.10
Max: 63.02
Average: 41.85
----- time module
06/05/2018
11:40:32
"""

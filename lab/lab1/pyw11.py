import subprocess

# check server status
## windows: ping 1.1.1.1
## linux: ping 1.1.1.1 -c 4
print("\nping 1.1.1.1")
ipaddr = "1.1.1.1"
result = subprocess.run(["ping",ipaddr], stdout=subprocess.PIPE, universal_newlines="\r\n")
print("return code:", result.returncode)
print(result.stdout)

# check our socket status
## netstat -ano
print("\nnetstat -ano")
result = subprocess.run(["netstat", "-ano"], stdout=subprocess.PIPE, universal_newlines="\r\n")
print("return code:", result.returncode)
print(result.stdout)

# Don't do these 
""" 
print("\nnetstat -an | findstr \"ESTABLISHED\"")
result = subprocess.run(["netstat", "-ano", "findstr", "ESTABLISHED"],
                        stdout=subprocess.PIPE, universal_newlines="\r\n")
print("return code:", result.returncode)
print(result.stdout) 
"""


""" Output
ping 1.1.1.1
return code: 0

Pinging 1.1.1.1 with 32 bytes of data:
Reply from 1.1.1.1: bytes=32 time=56ms TTL=55
Reply from 1.1.1.1: bytes=32 time=57ms TTL=55
Reply from 1.1.1.1: bytes=32 time=57ms TTL=55
Reply from 1.1.1.1: bytes=32 time=56ms TTL=55

Ping statistics for 1.1.1.1:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 56ms, Maximum = 57ms, Average = 56ms


netstat -ano
return code: 0

Active Connections

  Proto  Local Address          Foreign Address        State           PID
  TCP    0.0.0.0:135            0.0.0.0:0              LISTENING       1248
  TCP    0.0.0.0:445            0.0.0.0:0              LISTENING       4
  TCP    0.0.0.0:2179           0.0.0.0:0              LISTENING       5024
  ...
  TCP    10.0.1.158:56872       58.8.152.244:59982     SYN_SENT        11156
  TCP    10.0.75.1:139          0.0.0.0:0              LISTENING       4
  TCP    10.0.75.1:5040         0.0.0.0:0              LISTENING       8556
  ...
  TCP    127.0.0.1:49669        127.0.0.1:5354         ESTABLISHED     5280
  TCP    127.0.0.1:49670        127.0.0.1:5354         ESTABLISHED     5280
  ...
  TCP    172.17.127.145:5040    0.0.0.0:0              LISTENING       8556
  TCP    192.168.56.1:139       0.0.0.0:0              LISTENING       4
  TCP    [::]:445               [::]:0                 LISTENING       4
  TCP    [::]:2179              [::]:0                 LISTENING       5024
  ...                    
"""

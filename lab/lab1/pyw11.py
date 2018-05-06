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

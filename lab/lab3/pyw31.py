import crassh

# High rank user, no need to Enablepass
router = "10.0.1.22"
username = "admin"
password = "admin1234"
cmd01 = "show running-config"

# user need Enablepass, Not work in this lab because default enable=False
""" 
username = "cisco"
password = "ciscopass"
cmd01 = "show running-config"
** need to set option `enable=True` see pyw32.py 
"""

try:
    hostname = crassh.connect(router, username, password)
    print("Connected device %s [%s]" %(hostname,router))
    output = crassh.send_command(cmd01, hostname)
    print(output)
    crassh.disconnect()

except:
    print("Can not connect to [%s]" %router)

""" Output
Connecting to 10.0.1.22 ...
Connected device MNR-RT2 [10.0.1.22]
show running-config
Building configuration...

Current configuration : 1348 bytes
!
version 12.4
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname MNR-RT2
!
boot-start-marker
boot-end-marker
!
enable password enpass
!
no aaa new-model
!
!
ip cef
!
!
ip domain name mnr.local
ip auth-proxy max-nodata-conns 3
ip admission max-nodata-conns 3
!
!
voice-card 0
 no dspfarm
!
!
!
!
!
!
!
!
!
!
!
!
!
!
username cisco password 0 ciscopass
username admin privilege 15 password 0 admin1234
!
!
!
!
!
!
!
interface FastEthernet0/0
 no ip address
 shutdown
 duplex auto
 speed auto
!
interface FastEthernet0/1
 ip address 10.0.1.22 255.255.255.0
 duplex auto
 speed auto
!
interface Serial0/0/0
 no ip address
 shutdown
 no fair-queue
 clock rate 2000000
!
interface Serial0/1/0
 no ip address
 shutdown
 clock rate 125000
!
interface Serial0/1/1
 no ip address
 shutdown
 clock rate 125000
!
interface BRI0/2/0
 no ip address
 encapsulation hdlc
 shutdown
!
ip forward-protocol nd
ip route 0.0.0.0 0.0.0.0 10.0.1.1
!
!
ip http server
no ip http secure-server
!
access-list 1 permit 5.5.5.5
access-list 1 permit 1.2.3.4
access-list 1 permit 10.50.60.70
access-list 1 permit 10.0.1.174
snmp-server community public RO
!
!
!
control-plane
!
!
!
!
!
!
!
!
!
!
line con 0
line aux 0
line vty 0 4
 login local
line vty 5 15
 login local
!
scheduler allocate 20000 1000
!
end

MNR-RT2#
"""
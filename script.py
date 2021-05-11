import sys
from scapy.all import *
print("pinging the target....")
ip = "192.168.1.152"    # command line argument
icmp = IP(dst=ip)/ICMP()
resp = sr1(icmp,timeout=2)
if resp == None:
    print("This host is down")
else:
    print("This host is up")
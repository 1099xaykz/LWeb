from urllib2 import *
import os

a = open("recent_ip.txt", "r")
b = a.read()
ip = b.strip()
si = "http://api.hackertarget.com/subnetcalc/?q=" + ip
net = urlopen(si).read()
print (net)
exit()


from urllib2 import *

a = open("recent_ip.txt", "r")
b = a.read()
ip = b.strip()
link = "http://api.hackertarget.com/geoip/?q=" + ip
geoip = urlopen(link).read()
print (geoip)
exit()

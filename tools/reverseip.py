from urllib2 import *

a = open("recent_ip.txt", "r")
b = a.read()
ip = b.strip()
link = "http://api.hackertarget.com/reverseiplookup/?q=" + ip
si = urlopen(link).read()
print (si)
exit()

from urllib2 import *

a = open("recent_site.txt", "r")
b = a.read()
site = b.strip()
link = "http://api.hackertarget.com/httpheaders/?q=" + site
si =  urlopen(link).read()
print (si)
exit()

from urllib2 import *

a = open("recent_site.txt", "r")
b = a.read()
site = b.strip()
link = "http://api.hackertarget.com/hostsearch/?q=" + site
search = urlopen(link).read()
print (search)
exit()


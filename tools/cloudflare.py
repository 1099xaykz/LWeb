import socket
import sys
import time
from colorama import Fore
def start():
    subdom = ['ftp', 'cpanel', 'webmail', 'localhost', 'local', 'mysql', 'forum', 'driect-connect', 'blog', 'vb', 'forums', 'home', 'direct', 'forums', 'mail', 'access']
    a = open("recent_site.txt", "r")
    b = a.read()
    site = b.strip()
    if site == "":
        try:
            print(Fore.RED+" ! "+Fore.BLUE+"No se encontro sitio web")
            time.sleep(5)
            sys.exit()
        except:
            return
    for sub in subdom:
        try:
            hosts = str(sub) + "." + str(site)
            bypass = socket.gethostbyname(str(hosts))
            #print('Cloudflare Bypassed ! Real IP Address => '+bypass)
            print (" CloudFlare Bypass " + str(bypass) + ' - ' + str(hosts))
        except Exception:
            pass
    exit()

start()

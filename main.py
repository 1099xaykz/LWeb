import time
import os
import sys
import socket as s

BLACK = '\033[1;30m'
RED = '\033[1;31m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
MAGENTA = '\033[1;35m'
CYAN = '\033[1;36m'
WHITE = '\033[1;37m'
RESET = '\033[1;39m'

def redes():
	print(YELLOW + "⤜ " + RED + "TikTok: " + WHITE + "@ds.8mqk")
	print(YELLOW + "⤜ " + RED + "Telegram: " + WHITE + "@ds8mqk")
	print(YELLOW + "⤜ " + RED + "Instagram: " + WHITE + "@ds8mqk")

def banner():
	print(YELLOW + """
   __ _       _     _         _               _              _ 
  / /(_) __ _| |__ | |_ _ __ (_)_ __   __ _  | |_ ___   ___ | |
 / / | |/ _` | '_ \| __| '_ \| | '_ \ / _` | | __/ _ \ / _ \| |
/ /__| | (_| | | | | |_| | | | | | | | (_| | | || (_) | (_) | |
\____/_|\__, |_| |_|\__|_| |_|_|_| |_|\__, |  \__\___/ \___/|_|
        |___/                         |___/                    
""")
	print(RED + "              Japan Hacking group")

def main():
	banner()
	redes()
	print()
	print(YELLOW + "> " + RED + "Introduzca un nombre para el proyecto, ejemplo: " + WHITE + "hacking-argentina")
	project = input(YELLOW + "⟼ " + RED + "Proyecto > " + WHITE)
	os.system("cd projects && mkdir "+project)
	time.sleep(2)
	print(GREEN + "✔ " + WHITE + "La carpeta " + GREEN + "projects/" + project + WHITE + " fue creada correctamente")
	website = input(YELLOW + "⟼ " + RED + "Sitio web > " + WHITE)
	si = open("tools/recent_site.txt", "w")
	si.write(website)
	si.close()
	site = "projects/" + project + "/site"
	a = open(site, "w")
	a.write(website)
	a.close()
	ip = s.gethostbyname(website)
	no = open("tools/recent_ip.txt", "w")
	no.write(ip)
	no.close()
	ipruta = "projects/" + project + "/ip"
	b = open(ipruta, "w")
	b.write(ip)
	b.close()
	time.sleep(2)
	print(GREEN + "✔ " + WHITE + "Datos guardados...")
	time.sleep(1)
	print(YELLOW + "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
	print(YELLOW + "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
	print()
	print(GREEN + "IP: " + WHITE + ip)
	print(GREEN + "Sitio web: " + WHITE + website)
	print()
	print(YELLOW + "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
	print(YELLOW + "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
	print()
	print(GREEN + "Info de la IP: ")
	print(BLUE)
	os.system("cd tools && python3 iptracker.py")
	print()
	print(YELLOW + "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
	print(YELLOW + "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
	print()
	print(GREEN + "Subnet lookup: ")
	print(BLUE)
	os.system("cd tools && python2 subnet.py")
	print()
	print(YELLOW + "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
	print(YELLOW + "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
	print()
	print(GREEN + "Geo IP: ")
	print(BLUE)
	os.system("cd tools && python2 geoip.py")
	print()
	print(YELLOW + "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
	print(YELLOW + "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
	print()
	print(GREEN + "Host search: ")
	print(BLUE)
	time.sleep(2)
	os.system("cd tools && python2 hostsearch.py")
	print()
	print(YELLOW + "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
	print(YELLOW + "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
	print()
	print(GREEN + "Reverse ip lookup: ")
	print(BLUE)
	time.sleep(2)
	os.system("cd tools && python2 reverseip.py")
	print()
	print(YELLOW + "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
	print(YELLOW + "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
	print()
	print(GREEN + "DNS Lookup: ")
	print(BLUE)
	time.sleep(2)
	os.system("cd tools && python2 dnslookup.py")
	print()
	print(YELLOW + "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
	print(YELLOW + "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
	print()
	print(GREEN + "CloudFlare: ")
	print(BLUE)
	os.system("cd tools && python3 cloudflare.py")
	print()
	print(YELLOW + "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
	print(YELLOW + "⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯")
	print()
	print(GREEN + "CMS Detect: ")
	print(BLUE)
	os.system("cd tools && python3 cms.py")
	print()
	print(WHITE)
	exit()

if __name__=="__main__":
	main()

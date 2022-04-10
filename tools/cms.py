import requests, builtwith
from colorama import Fore
import sys
def start():
    a = open("recent_site.txt", "r")
    b = a.read()
    target = b.strip()
    if not 'https://' in target or not 'http://' in target:
        target = 'http://'+target
    info = builtwith.parse(target)
    for name in info:
        value = ''
        for val in info[str(name)]:
            name = name.replace('-',' ')
            name = name.title()
            value += str(val) 
        print(name+': '+value)

start()


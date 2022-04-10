import requests, json
import sys
from sys import argv
import os

red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

a = open("recent_ip.txt", "r")
b = a.read()
ip = b.strip()

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        print("IP:", data['query'])
        print("ISP:", data['isp'])
        print("Organizacion:", data['org'])
        print("Ciudad:", data['city'])
        print("Region:", data['region'])
        print("Longitude:", data['lon'])
        print("Latitude:", data['lat'])
        print("Zona horaria:", data['timezone'])
        print("Codigo postal:", data['zip'])
except requests.exceptions.ConnectionError as e:
        print("No hay conexion a internet")
exit()

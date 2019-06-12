# Import libraries
import requests
from urllib.request import urlopen, Request
import time
from bs4 import BeautifulSoup

print("Hola")

# Set the URL you want to webscrape from
url = "https://www.instant-gaming.com/es/"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

juego = input("Que juego quiere buscar?")
print("Quiere buscar " + juego)

html = urlopen(req)
res = BeautifulSoup(html.read(),"html.parser")

print(res.title)

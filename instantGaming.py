# Import libraries
from requests import get
from urllib.request import urlopen, Request
from requests.exceptions import RequestException
from contextlib import closing
import time
from bs4 import BeautifulSoup

print("Hola")

# Set the URL you want to webscrape from
url = "https://www.instant-gaming.com/es/"
req1 = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

juego = input("Que juego quiere buscar?")
print("Quiere buscar " + juego)

html = urlopen(req1)
res = BeautifulSoup(html.read(),"html.parser")

print(res.title)

urlbusqueda = "https://www.instant-gaming.com/es/busquedas/?query=" + juego
req2 = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

html = urlopen(req2)
res = BeautifulSoup(html.read(),"html.parser")
print(res.find('div', class_ = 'categoryBest item mainshadow'))





def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    print(e)
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from models import *
from datetime import datetime

datetime.now().strftime("%Y-%m-%d %H:%M")

url = ["https://www.computeruniverse.ru/products/90665621/asus-geforce-gtx1060-dual-6g.asp",
       "https://www.computeruniverse.ru/products/90580650/samsung-ssd-850-evo-basic-series.asp",
       "https://www.computeruniverse.ru/products/90480389/corsair-xms3-32gb-ddr3-kit.asp",
       "https://www.computeruniverse.ru/products/90481233/wd-blue-desktop.asp",
       "https://www.computeruniverse.ru/products/90597629/kingston-hyperx-savage.asp",
       "https://www.computeruniverse.ru/products/90568981/sandisk-ultra-ii-ssd-480gb.asp",
       "https://www.computeruniverse.ru/products/90665625/msi-geforce-gtx1060-armor-6g-oc-v1.asp"]
headers = {'user-agent': 'Mozilla/5.0 (X25; Linux x_4096) AppleWebKit/537.36 (KHTML, like Gecko) Ribin Chromium/91.0.65.110 Chrome/91.0.65.110 Safari/537.36'}

def get_price(url):
    r = requests.get(url, headers = headers).text
    soup = BeautifulSoup(r, 'html.parser')
    name = soup.find("h1", class_="producttitle fn").get_text()
    price_e = soup.find("span", class_="cartAreaPrice").get_text()
    price_r = soup.find("font", class_="oldpricebolditalic").get_text()
    price_r = price_r.replace("руб.", "").replace(" ", "")
    in_stock = soup.find("div", class_="statushelp_layer").find('strong').get_text()
    if in_stock == "на складе и готов к отправке":
        in_stock = "Ok"
    else:
        in_stock = "No"
    print('{0:<55} {1:<15} {2:<15} {3}'.format(name, price_e, price_r, in_stock))

def get_hardware(url):
    r = requests.get(url, headers = headers).text
    soup = BeautifulSoup(r, 'html.parser')
    name = soup.find("h1", class_="producttitle fn").get_text()
    print('{0:<55}'.format(name))
    Hardware.create(name=name, url=url)

for i in url:
    # get_price(i)
    get_hardware(i)
# for i in Hardware.select():
#     print(i.id, i.name, i.url)


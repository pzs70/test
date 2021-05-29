import urllib3
from bs4 import BeautifulSoup
#from urllib3 import PoolManager

url0 = "https://www.emag.hu"
url1 = "/solid-state-drive--ssd-meghajto/c?ref=hp_menu_quick-nav_7_17&type=category"


def callsite(u0, u1):
    http = urllib3.PoolManager()
    response = http.request('GET', u0 + u1)
    soup = BeautifulSoup(response.data.decode('utf-8'))
    return soup


response = callsite(url0, url1)
names=response.findAll("div", {"class": "card"})
for name in names:
    print(name) #.find("a",{"class": "product-title"}))

from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import prettytable
import os

q=input("關鍵字:")
t=prettytable.PrettyTable(["名稱", "價格"], encoding="utf-8")
p=1
url = f"https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={q}&page={p}&sort=sale/dc"
response = urlopen(url)
doodles=json.load(response)
t=prettytable.PrettyTable(["名稱", "價格"], encoding="utf-8")
for d in doodles['prods']:
    t.add_row([d['name'],d['price']])
print(t)
while True:
    p=input("前往頁碼:")
    os.system("cls")
    url = f"https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={q}&page={p}&sort=sale/dc"
    response = urlopen(url)
    doodles=json.load(response)
    t=prettytable.PrettyTable(["名稱", "價格"], encoding="utf-8")
    for d in doodles['prods']:
        t.add_row([d['name'],d['price']])
    print(t)

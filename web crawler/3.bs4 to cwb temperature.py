from urllib.request import urlopen
from bs4 import BeautifulSoup
import prettytable

response = urlopen("https://www.cwb.gov.tw/V8/C/W/TemperatureTop/County_TMax_T.html?ID=Wed%20Sep%2008%202021%2014:33:46%20GMT+0800%20(%E5%8F%B0%E5%8C%97%E6%A8%99%E6%BA%96%E6%99%82%E9%96%93)")
html = BeautifulSoup(response)
t=prettytable.PrettyTable(["地區", "氣溫"], encoding="utf-8")
for location, temperature in zip(html.find_all("th"), html.find_all("span", class_="tem-C is-active")):
	t.add_row([location.text, temperature.text])
print(t)

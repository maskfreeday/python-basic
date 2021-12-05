import requests
import codecs

#網路爬蟲作業
#get網路資料

r1 = requests.get(
    "http://teaching.bo-yuan.net/test/requests/",
    params={"action":"action"}
 )
r1.encoding= "utf-8"
print(r1.text)
#需要DELETE的操作。
r1 = requests.delete(
    "http://teaching.bo-yuan.net/test/requests/",
    params={"action":"action",},
    data={"id":"id"}
    )
r1.encoding= "utf-8"

print(r1.text)
#記得去PUT操作。
r1 = requests.put(
    "http://teaching.bo-yuan.net/test/requests/",
    params={"action":"action",},
    data={"id":"id","name":"name"}
 )
r1.encoding= "utf-8"

print(r1.text)
#PUT完了，也要PATCH資料。
r1 = requests.patch(
    "http://teaching.bo-yuan.net/test/requests/",
    params={"action":"action",},
    data={"id":"id","name":"name","address":"address"}
 )
r1.encoding= "utf-8"

print(r1.text)
#最後POST一筆資料吧。
r1 = requests.post(
    "http://teaching.bo-yuan.net/test/requests/",
    params={"action":"action",},
    data={"id":"id","name":"name","address":"address"}
)

r1.encoding= "utf-8"

print(r1.text)
#哈哈，答對了，請把操作過程中的所有指令保留在程式碼中，將檔案繳交上來。


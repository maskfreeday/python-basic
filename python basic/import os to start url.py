import sys
import os
url = sys.argv
# #sys.argv讀取cmd中，輸入的資料
if len(url)==2:
    os.system("start https://"+url[1])
else:
    print("請輸入網址")

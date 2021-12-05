import colorama
from colorama import Back
import time, sys, os

value = 'cls'
colorama.init(True)
os.system(value)


while 1:
  red, yellow, green = 5,1,4
  count = 0
  while red:
    count += 1
    red -= 1
    print(Back.RED + " ")
    print(str(count))
    time.sleep(1)
    os.system(value)
  while yellow:
    count += 1
    yellow -= 1
    print("\t" + Back.YELLOW + " ")
    print(str(count))
    time.sleep(1)
    os.system(value)
    
  while green:
    count += 1
    green -= 1
    print("\t\t" + Back.GREEN + " ")
    if count == 10:
      count = 0
    print( str(count))
    time.sleep(1)
    os.system(value)


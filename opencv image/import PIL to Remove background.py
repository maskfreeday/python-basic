import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
m1=cv2.imread("h2.png", 1)
B=m1[:,:,0].mean()
G=m1[:,:,1].mean()
R=m1[:,:,2].mean()
KB=(R+G+B)/(B*3)
KG=(R+G+B)/(G*3)
KR=(R+G+B)/(R*3)
m2=m1.copy()
# bgr藍  綠  紅
# 紅色 0 0  255    
# 綠色 0 255 0   
# 藍色 0 0 255 
# 黑色 0 0 0     
# 紅字 0 0 255  
# 白色  255  255  255

m3 = cv2.absdiff(m2, (0, 0, 255, 255)) # 減去紅色就會變成黑色
m4 = cv2.multiply(m3, (255, 255, 255, 255))  # 在讓黑色乘上白色
m5 = cv2.add(m4[:,:,2], m4[:,:,1])#加上1綠色2紅色
cv2.imshow("m5", m5)
cv2.waitKey(0)
cv2.destroyAllWindows()

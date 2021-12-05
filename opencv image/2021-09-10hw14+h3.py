import cv2
import numpy as np
# r  g  b
# 21 50 170
M1=cv2.VideoCapture("h3.mp4")
while M1.isOpened()==True:
	ret, frame=M1.read()#ret一定要是true才能讀取影片，m1是為讀取影片取一個變數，
	blurred_frame = cv2.GaussianBlur(frame,(5,5),0)
	hsv=cv2.cvtColor(blurred_frame,cv2.COLOR_BGR2HSV)#將bgr轉成hsv
	lower_color=np.array([100, 60, 0])
	upper_color=np.array([124, 255, 255])
	mask=cv2.inRange(hsv, lower_color, upper_color)#擷取要的顏色
	
	a, b=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)#儲存mask所有輪廓點
	# cv2.imshow("Frame",frame)
	# cv2.imshow("Mask",mask)
	for cnt in a:
		area = cv2.contourArea(cnt)
		# print(area)
		if area > 1000:
			peri = cv2.arcLength(cnt, True)
			approx = cv2.approxPolyDP(cnt,0.02 * peri,True)# 一般在對圖像取 contour 前, 都會先轉黑白, 做 threshold, canny 等 edge detection 處理, 能提高 contour 的辨識效果
			x , y,w,h = cv2.boundingRect(approx)
			cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)
			if ret==True:
				cv2.imshow("m3",frame)
				cv2.waitKey(33)

cv2.destroyAllWindows()
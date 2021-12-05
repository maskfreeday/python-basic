import cv2
import numpy as np
x1 = 0
x2 = 100
while True:
	if x2 != 500:
		x1+=1
		x2+=1
		m1=np.full((300, 500, 3), (255,255,255), np.uint8)
		m1=cv2.rectangle(m1, (x1,100), (x2,200), (255,0,0), -1)
		cv2.imshow("image",m1)
		if cv2.waitKey(1) != -1:#waitkey回傳值一定是-1，只要判斷不等於-1，就會導致程式繼續執行
			break#因此在後面設定一個break就可以讓程式停止運作，因此達到當x2為500時停住的作用
	else:
		while x2 != 100:
			x1-=1
			x2-=1
			m1=np.full((300, 500, 3), (255,255,255), np.uint8)
			m1=cv2.rectangle(m1, (x1,100), (x2,200), (255,0,0), -1)
			cv2.imshow("image",m1)
			if cv2.waitKey(1) != -1:
				break
cv2.destroyAllWindows()












	# else:


	# 	upcounting=50
	# 	dncounting=50
	# 	x1=x1-upcounting
	# 	x2=x2-dncounting
	# 	m1=np.full((300, 500, 3), (255,255,255), np.uint8)
	# 	m1=cv2.rectangle(m1, (x1,100), (x2,200), (255,0,0), -1)
		
	# 	cv2.imshow("image",m1)
	# 	cv2.waitKey(1)		
	# #else:
	# 	continue

# while True:
# 	if x1<0:
# 		upcounting=1
# 		dncounting=1
# 		x1=0-upcounting
# 		x2=500-dncounting
# 		m1=cv2.rectangle(m1, (x1,100), (x2,200), (255,0,0), -1)
# 		cv2.imshow("image",m1)
# 		cv2.waitKey(0)
# 	else:
# 		continue
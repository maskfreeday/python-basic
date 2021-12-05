import os

c=""
#資料夾列表
dir_list = []
  #檔案列表
file_list = []

for file_name in os.listdir():
  if os.path.isdir(file_name):
    dir_list.append(file_name)
  elif os.path.isfile(file_name):
    file_list.append(file_name)

  #計數器  
counter = 0

sycmd = ""
while c!="0":
	os.system("cls")
	#列出檔案
	if c =="1":
		if len(file_list) != 0:
			for file_name in file_list:
				print(counter," ",file_name)
				counter += 1
		else:
			print("沒有檔案")
	#列出資料夾
	elif c =="2":
		if len(dir_list) != 0:
			for dir_name in dir_list:
				print(counter," ",dir_name)
				counter += 1
		else:
			print("沒有資料夾")
	#顯示檔案內容
	elif c =="3":
		if len(file_list) != 0:
			for file_name in file_list:
				print(counter," ",file_name)
				counter += 1
				try:
					select = int(input("\n請輸入開啟檔案索引:"))
					file_name = file_list[select]
					with open(file_name,"r") as file:
						print(file.read())
				except:
					print("\n請輸入有效索引\n")
		else:
			print("沒有檔案")
	#刪除檔案
	elif c =="4":
		if len(file_list) != 0:
			for file_name in file_list:
				print(counter," ",file_name)
				counter += 1
				try:
					select = int(input("\n請輸入要刪除檔案索引:"))
					os.remove(file_list[select])
				except:
					print("\n請輸入有效索引\n")
		else:
			print("沒有檔案")
	# 執行檔案
	elif c =="5":
		if len(file_list) != 0:
			for file_name in file_list:
				print(counter," ",file_name)
				counter += 1
				try:
					select = int(input("\n請輸入要開啟的檔案索引:"))
					os.system(file_list[select])
				except:
					print("\n請輸入有效索引\n")
		else:
			print("沒有檔案")
	# 進入資料夾
	elif c =="6":
		if len(dir_list) != 0:
			for dir_name in dir_list:
				print(counter," ",dir_name)
				counter += 1
				try:
					select = int(input("\n請輸入要進入的資料夾索引:"))
					os.chdir(dir_list[select])
					print("現在目錄為:" + os.getcwd())
				except:
					print("\n請輸入有效索引\n")
		else:
			print("沒有資料夾")
	# 刪除資料夾
	elif c =="7":
		if len(dir_list) != 0:
			for dir_name in dir_list:
				print(counter," ",dir_name)
				counter += 1
				try:
					select = int(input("\n請輸入要刪除的資料夾索引:"))
					os.rmdir(dir_list[select])
				except:
					print("\n請輸入有效索引\n")
		else:
			print("沒有資料夾")

	# 回上層資料夾
	elif c =="8":
		os.chdir("..")
		print("現在目錄為:" + os.getcwd())

	print("工作路徑:",os.getcwd(),end="")
	print(""" (0) 離開程式
    	(1) 列出檔案
    	(2) 列出資料夾
    	(3) 顯示檔案內容
    	(4) 刪除檔案
    	(5) 執行檔案
    	(6) 進入資料夾
    	(7) 刪除資料夾
    	(8) 回上層資料夾
    """)
	c=input("操作:")
import pymysql
from pymysql import cursors
import prettytable
import os

root = input("請輸入資料庫root密碼：")
port= input("請輸入資料庫Port：")
while port == "3306":
    link = pymysql.connect(host="localhost", user="root", passwd="", db="python_ai", charset="utf8", port=3306,)
    cur = link.cursor()

    print("""
(0) 離開程式
(1) 顯示會員列表
(2) 新增會員資料
(3) 更新會員資料
(4) 刪除會員資料
(5) 新增會員的電話
(6) 刪除會員的電話
    """)
    sign = input("指令:")
     # (0)離開程式
    if sign == "0":
        break
    # (1) 顯示會員列表，要添加連上tel資料表的id去對上電話
    elif sign == "1":
        os.system('cls')
        # 建立prettytable架構
        prettytablelist = ["編號", "姓名", "生日", "地址","電話"]
        table = prettytable.PrettyTable(prettytablelist, encoding="utf-8")
        cur.execute('''SELECT
         `member`.`id`, 
         `member`.`name`,
         `member`.`birthday`,
         `member`.`address`,
         `tel`.`tel`
         FROM `member` LEFT JOIN `tel` ON `member`.`id`=`tel`.`member_id`''') 
        tmp=0
        for d in cur.fetchall():
            
            if tmp == d[0]:
                table.add_row([" "," "," "," ",d[4]])
            else:
                table.add_row(d)
            tmp=d[0]
        print(table)
        
    # (2)新增會員資料
    elif sign == "2":
        os.system('cls')
        name= input("請輸入會員姓名："),
        birthday= input("請輸入會員生日："),
        address= input("請輸入會員地址：")    
        cur.execute("""INSERT INTO `member`(`name`,`birthday`,`address`)
        VALUES(%s,%s,%s) """,[name,birthday,address])
        link.commit()
        
    # (3) 更新會員資料
    elif sign == "3":
        os.system('cls')
        # 建立prettytable架構
        prettytablelist = ["編號", "姓名", "生日", "地址","電話"]
        table = prettytable.PrettyTable(prettytablelist, encoding="utf-8")
        cur.execute('''SELECT
         `member`.`id`, 
         `member`.`name`,
         `member`.`birthday`,
         `member`.`address`,
         `tel`.`tel`
         FROM `member` LEFT JOIN `tel` ON `member`.`id`=`tel`.`member_id`''') 
        tmp=0
        for d in cur.fetchall():
            
            if tmp == d[0]:
                table.add_row([" "," "," "," ",d[4]])
            else:
                table.add_row(d)
            tmp=d[0]
        print(table)
        
        para = {"id": input("請選擇你要修改的資料編號:"),
                "name": input("請輸入會員姓名："),
                "birthday": input("請輸入會員生日："),
                "address": input("請輸入會員地址：")}
        cur.execute(""" UPDATE `member` SET
        `name`=%(name)s,`birthday`=%(birthday)s,
        `address`=%(address)s WHERE `id` = %(id)s""", para)
        cur.execute(""" SELECT * FROM `member`""")
        link.commit()        
    # (4)刪除會員資料
    elif sign == "4":
        os.system('cls')
        # 建立prettytable架構
        prettytablelist = ["編號", "姓名", "生日", "地址","電話"]
        table = prettytable.PrettyTable(prettytablelist, encoding="utf-8")
        cur.execute('''SELECT
         `member`.`id`, 
         `member`.`name`,
         `member`.`birthday`,
         `member`.`address`,
         `tel`.`tel`
         FROM `member` LEFT JOIN `tel` ON `member`.`id`=`tel`.`member_id`''') 
        tmp=0
        for d in cur.fetchall():
            
            if tmp == d[0]:
                table.add_row([" "," "," "," ",d[4]])
            else:
                table.add_row(d)
            tmp=d[0]
        print(table)

        id = input("請選擇你要刪除的資料編號:")
        cur.execute(f"DELETE FROM `member` WHERE `id`={id}")
        link.commit()
    #(5)新增會員的電話
    elif sign == "5":
        os.system('cls')
        # 建立prettytable架構
        prettytablelist = ["編號", "姓名", "生日", "地址","電話"]
        table = prettytable.PrettyTable(prettytablelist, encoding="utf-8")
        cur.execute('''SELECT
         `member`.`id`, 
         `member`.`name`,
         `member`.`birthday`,
         `member`.`address`,
         `tel`.`tel`
         FROM `member` LEFT JOIN `tel` ON `member`.`id`=`tel`.`member_id`''') 
        tmp=0
        for d in cur.fetchall():
            
            if tmp == d[0]:
                table.add_row([" "," "," "," ",d[4]])
            else:
                table.add_row(d)
            tmp=d[0]
        print(table)

        addid = input("請選擇要添加電話的會員編號：")
        phonenum = input("請輸入電話：")
        cur.execute("""INSERT INTO `tel`(`member_id`,`tel`) VALUES(%s,%s)""",[addid,phonenum])
        link.commit()
    	
    #(6) 刪除會員的電話
    elif sign == "6":
        os.system('cls')
        # 建立prettytable架構
        prettytablelist = ["編號", "姓名", "生日", "地址","電話"]
        table = prettytable.PrettyTable(prettytablelist, encoding="utf-8")
        cur.execute('''SELECT
         `member`.`id`, 
         `member`.`name`,
         `member`.`birthday`,
         `member`.`address`,
         `tel`.`tel`
         FROM `member` LEFT JOIN `tel` ON `member`.`id`=`tel`.`member_id`''') 
        tmp=0
        for d in cur.fetchall():
            
            if tmp == d[0]:
                table.add_row([" "," "," "," ",d[4]])
            else:
                table.add_row(d)
            tmp=d[0]
        print(table)

        deleteid = input("請選擇要刪除電話的會員編號：")

        prettytablelist = ["編號", "號碼"]
        table = prettytable.PrettyTable(prettytablelist, encoding="utf-8")
        cur.execute(f'''SELECT 
            `tel`.`id`,
            `tel`.`tel`
            FROM `tel` where `member_id`={deleteid}''') 
        for e in cur.fetchall():
            table.add_row(e) 
        print(table)


        phonenum = input("請輸入要刪除的電話編號：")
        cur.execute(f"DELETE FROM `tel` WHERE `id`={phonenum}")
        link.commit()
        
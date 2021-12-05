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
    """)
    sign = input("指令:")
     # (0)離開程式
    if sign == "0":
        break
    # (1) 顯示會員列表
    elif sign == "1":
        os.system('cls')
        # 建立prettytable架構
        prettytablelist = ["編號", "姓名", "生日", "地址"]
        table = prettytable.PrettyTable(prettytablelist, encoding="utf-8")
        cur.execute(""" SELECT * FROM `member`""")
        link.commit()
        for d in cur.fetchall():
            table.add_row(d)
        print(table)
        
    # (2)新增會員資料
    elif sign == "2":
        os.system('cls')
        para = {"name": input("name："),
                "birthday": input("birthday："),
                "address": input("address：")}
        cur.execute("""INSERT INTO `member`(`name`,`birthday`,`address`)
        VALUES(%(name)s,%(birthday)s,%(address)s) """, para)
        link.commit()
        
    # (3) 更新會員資料
    elif sign == "3":
        os.system('cls')
        prettytablelist = ["編號", "姓名", "生日", "地址"]
        table = prettytable.PrettyTable(prettytablelist, encoding="utf-8")
        cur.execute(""" SELECT * FROM `member`""")
        link.commit()
        for d in cur.fetchall():
            table.add_row(d)
        print(table)

        para = {"id": input("請選擇你要修改的資料編號:"),
                "name": input("請輸入會員姓名："),
                "birthday": input("請輸入會員生日："),
                "address": input("請輸入會員地址：")}
        cur.execute(""" UPDATE `member` SET
        `name`=%(name)s,`birthday`=%(birthday)s,
        `address`=%(address)s WHERE `id` = %(id)s""", para)
        
        link.commit()       
    # (4)刪除會員資料
    elif sign == "4":
        os.system('cls')
        prettytablelist = ["編號", "姓名", "生日", "地址"]
        table = prettytable.PrettyTable(prettytablelist, encoding="utf-8")
        cur.execute(""" SELECT * FROM `member`""")
        link.commit()
        for d in cur.fetchall():
            table.add_row(d)
        print(table)

        id = input("請選擇你要刪除的資料編號:")
        cur.execute(f"DELETE FROM `member` WHERE `id`={id}")
        link.commit()
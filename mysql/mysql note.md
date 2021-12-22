## mysql
資料庫本身就是存放資料的地方
資料整理可用軟體就是資料庫管理系統(DBMS, database management system)
透過資料庫管理系統有效率將資料存好，並且管理好位置

可用軟體主要分為
1. 關聯式資料庫(RDBMS,Relational =SQL資料庫):把資料用一個一個表格存放起來，再用關聯存起來
- MySQL
- Oracle
- PostgreSQL
- SQL server

ACID，是指資料庫管理系統（DBMS）在寫入或更新資料的過程中，為保證事務（transaction）是正確可靠的，所必須具備的四個特性：
- 原子性（Atomicity，或稱不可分割性）:所有操作，不是全部完成或全部不完成，不會結束在中間某個環節。如果中間有錯會回覆到為進行更改前的樣子。
- 一致性（Consistency):在事務開始之前和事務結束以後，資料庫的完整性沒有被破壞。這表示寫入的資料必須完全符合所有的預設約束、觸發器、級聯回滾等
- 隔離性（Isolation，又稱獨立性）:資料庫允許多個並發事務同時對其數據進行讀寫和修改的能力，隔離性可以防止多個事務並發執行時由於交叉執行而導致數據的不一致。事務隔離分為不同級別，包括未提交讀（Read uncommitted）、提交讀（read committed）、可重複讀（repeatable read）和串行化（Serializable）
- 持久性（Durability）:事務處理結束後，對數據的修改就是永久的，即便系統故障也不會丟失。

2. 非關聯式資料庫(NRDMBS,not just sql / noSQL) :儲存方式會根據軟體不同
- MongoDB:文件導向的資料庫管理系統，用C++等語言撰寫而成
- Redis:一個使用ANSI C編寫的開源、支援網路、基於記憶體、分散式、可選永續性的鍵值對儲存資料庫。
- DynamoDB:Amazon DynamoDB是一個支援鍵-值儲存和文件型資料結構的NoSQL資料庫服務，是亞馬遜雲端運算服務的一部分。
- Elastricsearch

SQL :是拿來跟 RDMBS做溝通用。
是一種特定目的程式語言，用於管理關聯式資料庫管理系統（RDBMS），或在關係流資料管理系統（RDSMS）中進行流處理。

MySQL 免費而且最有名

table and keys
將資料儲存成表格在座關聯
表格=table
內容=key
column 列↓ 一個屬性
row -> 一筆資料
id=primary key主鍵=唯一表示每一筆資料=通常橘色背景

| id | name | major |
| ---- | ---- | ---- |
| 1 |  ----  | ----  |
| 2 |  ----  | ----  |
| 3 |  ----  | ----  |
| 4 |  ----  | ----  |
| 5 |  ----  | ----  | 

| email | password | date_created |
| ---- | ---- | ---- |
| 1 |  ----  | ----  |
| 2 |  ----  | ----  |
| 3 |  ----  | ----  |
| 4 |  ----  | ----  |
| 5 |  ----  | ----  | 

如果公司想要增加新的部門屬性
可以再新增一個資料庫並且將branch id新增到

##branch

| branch_id | branch_name | 
| ---- | ---- |
| 1 |  研發  |
| 2 |  生產  |
| 3 |  品保  |
| 4 |  行銷  |
| 5 |  管理  |

primary key
其實可以一次使用兩個
![](https://i.imgur.com/j6zurKF.png)

也也可以設定成三四個都行
37:00

進入Workbench程式畫面
![](https://i.imgur.com/fqVpTxD.png)

創建資料庫
展示資料庫

mysql關鍵字:mysql語法，為藍色
建議使用大寫區別語法跟命名名稱
命名名稱建議使用 
```
CREATE DATABASE `database`;
SHOW DATABASES;
DROP DATABASE `database`;
```

常見指令
![](https://i.imgur.com/qTt9XNv.png)
```
INT 
DECIMAL(M,N) M:總共有幾位數 N:小數點後占幾位 
VARCHAR(N) 字串:純文字,M:最多可以存放幾個字元
BLOB 
DATE
TIMESTAMP
```


實際練習
建立表格
![](https://i.imgur.com/v0qHMsj.png)
![](https://i.imgur.com/PAAyKVF.png)
也可以更改寫法
```
CREATE TABLE `student`(
	`student_id` INT PRIMARY KEY,
    `name` VARCHAR(20),
    `major` VARCHAR(20),
    PRIMARY KEY(`student_id`)
    );	
```

增加屬性(TABLE)
```
ALTER TABLE `student` ADD gpa DECIMAL(3,2);    
```
gpa指的是屬性名稱
DECIMAL(3,2) 給他一個範圍值 0.00

刪除屬性
```
ALTER TABLE `student` DROP COLUMN gpa;
```
存入資料(data) INSERT

![](https://i.imgur.com/i6gmUo0.png)

INSERT 資料庫 VALUES(`student_id`,`name`,`major`)

也可以透過新增時，加入`NULL`，跳過要輸入的值

```
INSERT INTO `student` VALUES(1, '小白', '歷史');
INSERT INTO `student` VALUES(2, '小黑', '生物');
INSERT INTO `student` VALUES(3, '小綠', NULL);

INSERT INTO `student` (`name`, `major`, `student_id`)VALUES( '小藍', '英語', 4);
INSERT INTO `student` ( `major`, `student_id`)VALUES( '英語', 5);
SELECT * FROM `student`; 
```

**限制約束語法(constraints)**  
在創建表格時就可以先行對表格的輸入值做預設  
對此表格自動照順序新增Primary key  
姓名: 20字以內 不可為空值
主修科目: 20字以內 預設為歷史
```
CREATE TABLE `student01`(
	`student_id01` INT AUTO_INCREMENT,
    `name` VARCHAR(20) NOT NULL,
    `major` VARCHAR(20) DEFAULT '歷史',
    PRIMARY KEY(`student_id01`)
);	

NOT NULL 不能為空值
UNIQUE 只能是唯一一個值
DEFAULT 預設為
```
透過新增value進行測試
```
INSERT INTO `student01` VALUES(1, '小白', '歷史');
INSERT INTO `student01` VALUES(2, '小黑', '生物');
INSERT INTO `student01` VALUES(3, '小綠', NULL);
    
INSERT INTO `student01` (`name`, `major`)VALUES( '小藍', '英語');    
SELECT * FROM `student01`; 
```

![](https://i.imgur.com/NvMMc0o.png)

**修改、刪除資料**

首先你要先重新建立好資料庫
```
CREATE DATABASE `database`;
SHOW DATABASES;
USE `sql_tutorial`;
```
創建表格

```
CREATE TABLE `student02`(
	`student_id` INT AUTO_INCREMENT,
    `name` VARCHAR(20),
    `major` VARCHAR(20),
    `score` INT,
    PRIMARY KEY(`student_id`)
);	
```
輸入好的值

```
INSERT INTO `student02` VALUES( 1, '小白', '歷史', 50);
INSERT INTO `student02` VALUES( 2, '小黃', '生物', 90);
INSERT INTO `student02` VALUES( 3, '小綠', '英文', 70);
INSERT INTO `student02` VALUES( 4, '小藍', '數學', 80);
INSERT INTO `student02` VALUES( 5, '小紫', '公民', 20);
```
![](https://i.imgur.com/2waytzv.png)

再來就可以修改輸入

首先因為mysql有個叫SQL_SAFE_UPDATES的變數

開啟的狀態下，在沒有 WHERE 或 LIMIT 條件的 UPDATE 或 DELETE 動作會拒絕執行而即使是有 WHERE 和 LIMIT 條件，但沒有 KEY column 的 WHERE 條件也會拒絕執行。
因此必須加入  

SET 要改成甚麼   
WHERE 條件:要去哪邊改資料
```
SET SQL_SAFE_UPDATES=0; 關閉安全模式
UPDATE `student02` SET `major` = '英語文學' WHERE `major` = '英文';
SET SQL_SAFE_UPDATES=1; 開啟安全模式
```
![](https://i.imgur.com/CWt5JLX.png)

也可以選擇修改第幾個student_id 後再進行修改裡面的major
```
UPDATE `student02` SET `major` = '生物' WHERE `student_id` = 4;
```
![](https://i.imgur.com/7NrnaWT.png)

也可以一次修改多個條件
例如將歷史跟生物都改成 生物演化


```
UPDATE `student02` SET `major` = '生物演化' WHERE `major` = '歷史' or `major` = '生物';
```
![](https://i.imgur.com/KAnIhPx.png)

```
UPDATE `student02` SET `name` = '小灰', `major` = '物理' WHERE `student_id` = 1;
```

![](https://i.imgur.com/TIgeF5Z.png)
```
UPDATE `student02` SET `major` = '物理';
```
![](https://i.imgur.com/EblMieI.png)

刪除資料  
透過條件不同都可以修改

```
DELETE FROM `student02` WHERE `student_id`=4;
```
![](https://i.imgur.com/pbRrExj.png)  
也可以對條件增加and 讓兩者都符合的資料才做刪除

```
DELETE FROM `student02` WHERE `name` ='小灰' AND `major` = '物理';
```
![](https://i.imgur.com/IIVvhLh.png)

也可以透過分數高低建立條件去做刪除

```
DELETE FROM `student02` WHERE `score` < 60;
```
![](https://i.imgur.com/p1MTNgd.png)

以下是
常用的比較符號
```
>大於
<小於
>= 大於等於
<= 小於等於
= 等於
<> 不等於
```
也可以做不給where 條件做判斷
就變成刪除整個表格

```
DELETE FROM `student02`;
```
![](https://i.imgur.com/tR68gC6.png)

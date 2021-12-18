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
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

**取得資料**  
取得全部表格中資料，可以透過選擇由甚麼做排序
order by 排序
desc 由高到低
LIMIT 限制一次要讀取的值有幾個
```
SELECT * FROM `student02` ORDER BY `score` DESC LIMIT 3;
```
![](https://i.imgur.com/dUnRfYV.png)

也可以在搜尋資料時加上條件
where 
and
or

```
SELECT * FROM `student02` WHERE `major` = '歷史' and `student_id` = 1;
```
![](https://i.imgur.com/40zgS0Q.png)

```
SELECT * FROM `student02` WHERE `major` = '英文' OR `score` >20;
```

![](https://i.imgur.com/HWXa7og.png)

也可以把上面的全部功能都混用
搜尋主修是英文或分數不等於70分的
列出前面兩個
```
SELECT * FROM `student02` WHERE `major` = '英文' OR `score` <>70  limit 2;
```
![](https://i.imgur.com/Ymnb5ra.png)


IN('歷史','英語',生物)=`major` = '歷史' OR `major` = '英文' `major` = '生物'
簡單說IN = OR OR....
這個功能也可以跟前面的DESC AND OR 混用
```
SELECT * FROM `student02` WHERE `major` IN('歷史','英文','生物'); 
```
![](https://i.imgur.com/ArAuQ5w.png)

模擬創建公司資料庫
員工表格  

```
CREATE TABLE `employee`(
	`emp_id` INT PRIMARY KEY,
    `name` VARCHAR(20),
    `birth_date` DATE,
    `sex` VARCHAR(1),
    `salary` INT,
    `branch_id` INT,
    `sup_id` INT
);	
```  
員工編號 一定只能有一個所以設定為PRIMARY  
NAME 只要設定長度20以內即可  
生日就直接設定為DATE  
性別 通常為男或女 直接設定長度1即可  
branch_id 部門編號 設定為整數即可  
sup_id 主管編號 設定為整數即可  


部門表格  
 On Delete 或 On Update：當發生刪除或更新動作時，依後面宣告處理。
 ON UPDATE SET NULL
 ON DELETE SET NULL
 這兩個功能可以幫助在設計MYSQL表格時，以後要刪除資料或是更新資料時方便使用
```
CREATE TABLE `branch`(
	`branch_id` INT PRIMARY KEY,
    `branch_name` VARCHAR(20),
    `manager_id` INT,
    foreign key (`manager_id`) REFERENCES `employee` (`emp_id`) ON DELETE SET NULL
);

```
部門編號 設定為主鍵  
部門名稱 名稱為二十字以內  
員工編號 整數並且引用`employee`表格中的`emp_id`，並且當要刪除時只會將該格設定為NULL


新增外鍵

再來是新增表格屬性的部分

這邊補充個知識
一個Table表中只能有一個主鍵，但是可以有很多外鍵。主鍵與外鍵的配對就形成了Relational 關聯性 ，所以才稱作Relational database 關聯性資料庫。

因此為兩個表格中有互相需要引用到的部分，進行更改資料庫結構，新增外鍵進行表格之間的關聯性建立

ALTER TABLE 是用來對已存在的資料表結構作更改。
FOREIGN KEY外鍵 新增外鍵

```
ALTER TABLE `employee`
ADD FOREIGN KEY(`branch_id`)
REFERENCES `branch` (`branch_id`)
ON DELETE SET NULL;

ALTER TABLE `employee`
ADD FOREIGN KEY(`sup_id`)
REFERENCES `employee` (`emp_id`)
ON DELETE SET NULL;
```
更改`employee`表格屬性
增加 外鍵 `branch_id`的屬性引用 表格`branch`的`branch_id`
如果刪除就設定為null

更改`employee`表格屬性
增加 外鍵 `sup_id`的屬性引用 表格`employee`的`emp_id`
如果刪除就設定為null

客戶表格

```
CREATE TABLE `client`(
	`client_id` INT PRIMARY KEY,
    `client_name` VARCHAR(20),
    `phone` VARCHAR(20)
);
```
客戶編號 一定只能有一個所以設定為PRIMARY  
NAME 只要設定長度20以內即可  
電話號碼 只要設定長度20以內即可  


銷售金額表格
works_with
客戶跟銷售員工的表格建立

Cascade：所有關聯的紀錄也會跟隨刪除或更新。

```
CREATE TABLE `works_with`(
	`emp_id` INT,
    `client_id` INT,
    `total_sales` INT,
    PRIMARY KEY(`emp_id`,`client_id`),
    FOREIGN KEY(`emp_id`) REFERENCES `employee`(`emp_id`) ON DELETE CASCADE,
    FOREIGN KEY(`client_id`) REFERENCES `client`(`client_id`) ON DELETE CASCADE);
```
創建銷售金額表格
建立`emp_id`，引用`employee`表格的`emp_id`資料 並且當有一邊資料刪除時會連同員工資料一同刪除
建立`client_id`，引用`client`表格的`client_id`資料 並且當有一邊資料刪除時會連同顧客資料一同刪除
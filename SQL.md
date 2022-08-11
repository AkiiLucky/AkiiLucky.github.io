<style type="text/css">
    h1 { counter-reset: h2counter; }
    h2 { counter-reset: h3counter; }
    h3 { counter-reset: h4counter; }
    h4 { counter-reset: h5counter; }
    h5 { counter-reset: h6counter; }
    h6 { }
    h2:before {
      counter-increment: h2counter;
      content: counter(h2counter) ".\0000a0\0000a0";
    }
    h3:before {
      counter-increment: h3counter;
      content: counter(h2counter) "."
                counter(h3counter) ".\0000a0\0000a0";
    }
    h4:before {
      counter-increment: h4counter;
      content: counter(h2counter) "."
                counter(h3counter) "."
                counter(h4counter) ".\0000a0\0000a0";
    }
    h5:before {
      counter-increment: h5counter;
      content: counter(h2counter) "."
                counter(h3counter) "."
                counter(h4counter) "."
                counter(h5counter) ".\0000a0\0000a0";
    }
    h6:before {
      counter-increment: h6counter;
      content: counter(h2counter) "."
                counter(h3counter) "."
                counter(h4counter) "."
                counter(h5counter) "."
                counter(h6counter) ".\0000a0\0000a0";
    }
</style>




# SQL 常用命令

## 创建数据库
```sql
--CREATE DATABASE 数据库名
CREATE DATABASE `school` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */ /*!80016 DEFAULT ENCRYPTION='N' */
```

## 创建表
```sql
/*
CREATE TABLE IF NOT EXISTS 表名 (
    `字段名` 数据类型 [约束1] [约束2] [约束3] [...] [注释],
    `字段名` 数据类型 [约束1] [约束2] [约束3] [...] [注释],
    PRIMARY KEY(主键) 
)ENGINE=引擎名, DEFAULT CHARSET=字符集编码
*/
CREATE TABLE `student1` (
  `id`  int(10) NOT NULL AUTO_INCREMENT COMMENT '学号',
  `name` varchar(40) NOT NULL DEFAULT '匿名' COMMENT '姓名',
  `password` varchar(10) NOT NULL DEFAULT '123456' COMMENT '密码',
  `age` int NOT NULL COMMENT '年龄',
  `date` datetime NOT NULL COMMENT '注册日期',
  `email` varchar(20) NOT NULL COMMENT '邮箱',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
```

## 删除表
```sql
DROP TABLE IF EXISTS 表名
```

## 显示表的结构
```sql
desc '表名'
```

## 修改表

### 修改表名
```sql
--ALTER TABLE 旧表名 RENAME AS 新表名
ALTER TABLE `student1` RENAME AS `student2`
```

### 增加表的字段
```sql
--ALTER TABLE 旧表名 ADD 字段名 字段属性...
ALTER TABLE `student2` ADD `address` VARCHAR(1024) COMMENT '地址'
```

### 删除表的字段
```sql
ALTER TABLE `student2` DROP `address`
```

### 修改表的字段
```sql
--修改约束
ALTER TABLE `student2` MODIFY `address` VARCHAR(2048);

--修改字段名
ALTER TABLE `student2` CHANGE `address` `Address`  VARCHAR(2048);

/*
相同点：都是用来改变字段的属性，change和modify执行成功后都会这本次设置的属性替换字段原属性
不同点：重命名只能使用change
*/
```

### 添加外键
```sql
ALTER TABLE `student01` 
ADD CONSTRAINT `FK_gradeid` FOREIGN KEY(`gradeid`) REFERENCES `grade`(`gradeid`);
```

##  DML语言 (数据库管理语言)

### 增加记录 insert
```sql
--INSERT INTO 表名(字段名1,字段名2,字段名3...) VALUES (值1,值2,值3...)
INSERT INTO `student2`(`name`,`password`,`age`) VALUES ('小埋','123456',16)
```

### 更改记录 update
```sql
--UPDATE 表名 SET 字段名1=值1[,字段名2=值2,字段名3=值3...] [WHERE 条件1 AND 条件2 AND 条件3...]
UPDATE `student2` SET `name`='张三' WHERE `id` = 1;
UPDATE `student2` SET `age`=20, `email`='123456@qq.com' WHERE `name` = '张三' AND `id` = 1 ;
```

### 删除记录 delete
```sql
--DELETE FROM 表名 [WHERE 条件1 AND 条件2 AND 条件3...]
DELETE FROM `student2` WHERE `name` = '张三' 

--TRUNCATE TABLE 表名
TRUNCATE TABLE `student2`

/*
DELETE FROM 与 TRUNCATE TABLE 的区别
DELETE FROM 是一条一条删除记录，不改变自增计数器
DELETE FROM 是清空所有记录，自增计数器被重置
*/
```

## DQL语言 (数据库查询语言)


### select 字段名 from 表名

```sql
--查询全部字段
SELECT * FROM `student`
--查询指定字段
SELECT `studentno`, `studentname` FROM `student` AS 学生表
```

### AS 关键字用于取别名

```sql
SELECT `studentno` AS 学号, `studentname` AS 姓名 FROM `student` AS 学生表
```

### distinct 关键字用于去除重复数据

```sql
SELECT DISTINCT `studentno` AS 学号 FROM  `result`
```


### select 表达式 from 表名

```sql
--数据库中的表达式：文本值，NULL，函数，字段名，算术表达式，系统变量

SELECT VERSION() --数据库版本 （函数）

SELECT 1+63*2 AS 计算结果 --（算术表达式）

SELECT @@auto_increment_increment --自增的步长（变量）
```

### 函数 concat

```sql
SELECT CONCAT('姓名: ',`studentname`) AS 姓名 FROM `student`
```

### where 条件查询

```sql
SELECT `studentno` AS 学号, `studentresult` AS 成绩 FROM `result` 
WHERE `studentresult` > 80;

SELECT `studentno` AS 学号, `studentresult` AS 成绩 FROM `result` 
WHERE `studentresult` >= 80 AND `studentresult` <= 90;

SELECT `studentno` AS 学号, `studentresult` AS 成绩 FROM `result` 
WHERE `studentresult` BETWEEN 80 AND 90;

SELECT `studentno` AS 学号, `studentresult` AS 成绩 FROM `result` 
WHERE `studentresult` != 80;

SELECT `studentno` AS 学号, `studentresult` AS 成绩 FROM `result` 
WHERE NOT `studentresult` = 80;
```

### 模糊查询

#### like
```sql
-- % 代表零个或多个任意字符, _ 代表一个任意字符

SELECT `subjectname` AS 课程号,`subjectname` AS 课程名, `classhour` AS 课时 FROM `subject`
WHERE `subjectname` LIKE '%C语言%'

SELECT `subjectname` AS 课程号,`subjectname` AS 课程名, `classhour` AS 课时 FROM `subject`
WHERE `subjectname` LIKE '高等数学-_'

```
#### in
```sql
SELECT `subjectname` AS 课程号,`subjectname` AS 课程名, `classhour` AS 课时 FROM `subject`
WHERE `subjectname` IN ('高等数学-1','高等数学-2')
```
#### is null 
```sql
SELECT `subjectname` AS 课程号,`subjectname` AS 课程名, `classhour` AS 课时 FROM `subject`
WHERE `subjectname` IS NULL

SELECT `subjectname` AS 课程号,`subjectname` AS 课程名, `classhour` AS 课时 FROM `subject`
WHERE `subjectname` IS NOT NULL
```



### 联表查询 join on

#### inner join 
```sql
--TableA inner join TableB  从多个表中返回满足 JOIN 条件的所有行
SELECT s.`studentno` AS 学号,`studentname` AS 姓名, `subjectno` AS 课程号, `studentresult` AS 课程成绩
FROM `student` AS s
INNER JOIN `result` AS r
ON s.`studentno` = r.`studentno`; 
```
#### left join 
```sql
--LEFT JOIN 即使右表中没有匹配，也从左表返回所有的行
--例：查询未参加考试的同学
SELECT s.`studentno` AS 学号,`studentname` AS 姓名, `subjectno` AS 课程号, `studentresult` AS 课程成绩
FROM `student` AS s
LEFT JOIN `result` AS r
ON s.`studentno` = r.`studentno`
WHERE `studentresult` IS NULL 
```
#### right join
```sql
--RIGHT JOIN 即使左表中没有匹配，也从右表返回所有的行
--例：查询参加考试的学生的所有课程信息及成绩
SELECT stu.`studentno` AS 学号,stu.`studentname` AS 姓名, res.`subjectno` AS 课程号,sub.`subjectname` AS 课程名, res.`studentresult` AS 课程成绩
FROM `student` AS stu
RIGHT JOIN `result` AS res 
ON stu.`studentno` = res.`studentno`
INNER JOIN `subject` AS sub
ON res.`subjectno` = sub.`subjectno`
```

### 自查询

```sql
SELECT father.`categoryid` AS '父栏目id',father.`categoryname` AS '父栏目名称', son.`categoryid` AS '子栏目id', son.`categoryname` AS '子栏目名称'
FROM `category` AS father, `category` AS son
WHERE father.`categoryid` = son.`pid`
```
### 排序 order by 字段名 asc/desc

```sql
SELECT * 
FROM `result`
ORDER BY `studentresult` ASC --升序

SELECT * 
FROM `result`
ORDER BY `studentresult` DESC --降序
```
### 分页 limit 起始记录索引,页面记录数

```sql
SELECT * 
FROM `subject`
ORDER BY `subjectno` ASC
LIMIT 0,5 --从第一条记录开始，显示5条记录
```
### 嵌套查询 

```sql
--在where里面可以嵌套select查询的结果
SELECT `studentname`,`studentno`
FROM `student` s
WHERE `studentno` IN (
	SELECT DISTINCT `studentno`
	FROM `result`
	WHERE `subjectno` = (
		SELECT `subjectno`
		FROM `subject`
		WHERE `subjectname` = '高等数学-1' 
	) AND `studentresult` > 60
)
```

### 分组及分组过滤

```sql
SELECT `subjectname` AS 课程名,AVG(`studentresult`) AS 平均分, SUM(`studentresult`) AS 总分
FROM `subject` s
INNER JOIN `result` r
ON s.`subjectno` = r.`subjectno`
GROUP BY `subjectname` --分组
HAVING 平均分 > 60 AND 总分 > 100 --过滤
```



## MySQL函数

### 常用函数 http://c.biancheng.net/mysql/function/

```sql
-- 时间
SELECT NOW() --当前时间
SELECT YEAR(NOW())
SELECT MONTH(NOW())
SELECT DAY(NOW())
SELECT HOUR(NOW())
SELECT MINUTE(NOW())
SELECT SECOND(NOW())

-- 系统
SELECT USER()
SELECT VERSION()
```
### 聚合函数

#### 计数
```sql

count(*) --包括了所有的列，相当于行数，在统计结果的时候， 不会忽略列值为NULL  
count(1) --包括了忽略所有列，用1代表代码行，在统计结果的时候， 不会忽略列值为NULL  
count(列名) --只包括列名那一列，在统计结果的时候，会忽略列值为空（这里的空不是只空字符串或者0，而是表示null）的计数， 即某个字段值为NULL时，不统计。
/*
列名为主键，count(列名)会比count(1)快  
列名不为主键，count(1)会比count(列名)快  
如果表多个列并且没有主键，则 count（1） 的执行效率优于 count（*）  
如果有主键，则 select count（主键）的执行效率是最优的  
如果表只有一个字段，则 select count（*）最优。
*/
```

### 加密函数

```sql
SELECT MD5('123456')
```

## 事务

### 事务的基本原则 ACID

#### 原子性 （Atomicity）
要么都成功，要么都失败

#### 一致性 （Consistency）
事务提交后的数据要保持一致

#### 隔离性 （Isolation）
隔离性是当多个用户并发访问数据库时，比如操作同一张表时，数据库为每一个用户开启的事务，不能被其他事务的操作所干扰，多个并发事务之间要相互隔离。

#### 持久性 （Isolation）
事务提交后的数据持久化保存在数据库中，提交后不可逆

### 隔离所导致的一些问题

#### 脏读
一个事务读取了另一个事务未提交的数据

#### 不可重复读
一个事务读取表中某一行时，多次读取的结果不同

#### 虚读或幻读
在一个事务内读取到了另一个事务插入的数据，导致前后数据读取不一致




### 手动模拟事务执行过程

```sql
CREATE DATABASE shop CHARACTER SET utf8 COLLATE utf8_general_ci;
USE shop;

CREATE TABLE `account` (
	`id` INT(10) NOT NULL AUTO_INCREMENT COMMENT '账户id',
	`name` VARCHAR(30) NOT NULL COMMENT '姓名',
	`money` DECIMAL(9,2) NOT NULL COMMENT '账户余额', /*小数点前最多9位，小数点后2位*/
	PRIMARY KEY(`id`)
)ENGINE=INNODB, DEFAULT CHARSET=utf8;

INSERT INTO `account`(`name`,`money`) 
VALUES ('A',1000),('B',1000);

/*
模拟事务的执行过程
例：转账过程
*/
/*关闭自动提交*/
SET autocommit = 0; 
/*开启一个(组)事务*/
START TRANSACTION;
/*执行事务的多条SQL语句*/
UPDATE `account` SET `money`=`money`-500 WHERE `name` = 'A';
UPDATE `account` SET `money`=`money`+500 WHERE `name` = 'B';
/*提交事务,数据持久化*/
COMMIT;
/*回滚*/
ROLLBACK;
/*开启自动提交*/
SET autocommit = 1; 
```


## 索引

### 索引分类
#### 主键索引（PRIMARY KEY）
一张数据表只能有一个主键索引，索引列值不允许有空值，通常在创建表时一起创建。
#### 唯一索引 （UNIQUE KEY）
建立在UNIQUE字段上的索引被称为唯一索引，一张表可以有多个唯一索引，索引列值允许为空，列值中出现多个空值不会发生重复冲突。
#### 普通索引 （KEY/INDEX）
建立在普通字段上的索引被称为普通索引。默认为普通索引。
#### 全文索引 （FULLTEXT）
部分引擎才有，用于快速定位数据

### 使用方法 （创建表时添加或创建表后再添加）
```sql
-- 显示索引
SHOW INDEX FROM student

-- 添加全文索引
ALTER TABLE `school`.`student` ADD FULLTEXT INDEX `studentname`(`studentname`)

-- 分析sql执行情况
EXPLAIN SELECT * FROM `student`
EXPLAIN SELECT * FROM `student` WHERE MATCH(`studentname`) AGAINST('张伟')
```

### 索引原则
 - 索引不是越多越好
 - 经常变动的数据不要加索引
 - 小数据量的表不需要加索引
 - 索引一般加在经常查询的字段上


## 权限管理
```sql

```

## 备份
```sql
mysqldump 
```

## 三大范式
### 第一范式（1NF）
原子性：保证每一列不可再分
### 第二范式（2NF）
前提：满足第一范式
每张表只描述一个事情
### 第三范式（3NF）
前提：满足第一范式和第二范式
要确保表的每一列都与主键直接相关，不能间接相关

### 规范性 vs 性能
- 关联查询的表不能超过三张
- 要考虑数据库的性能，有时也可以违反三大范式，故意增加一些冗余列，将多表查询变为单表查询
```sql

```

##
```sql

```
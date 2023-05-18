```
host        -h  主机
port        -P  端口号   （大写）
user        -u  用户名
password    -p  密码     （小写）
```

注释
```mysql
-- 单行注释
# 单行注释
多行注释  /*     */
```

连接数据库
mysql -h127.0.0.1 -P3306 -uroot -proot  -- 明文
如果连接本地数据库 -h可以省略 如果服务器端口是3306，-P端口号也可以省略
mysql -uroot -proot

密文输入密码
mysql -uroot -p  

退出
exit 
quit
\q


创建数据库
```
create database [if not exists] 数据名 [选项]
```
 create database stu;
 在创建数据库时候，判断数据库是否存在，不存在就创建
 create database if not exists stu;

 特殊字符、关键字做数据库名，使用反引号将数据库名括起来
 create database `create`;

 创建数据库时指定存储的字符编码
 create database emp charset=gbk;


  显示所有数据库
 ```
show databases;
```
 删除数据库
```
drop database [if exists] 数据库名
```
drop database `create`;
判断数据库是否存在，如果存在就删除
drop database if exists stu;

创建表
create table stu1(
    -> id tinyint,      
    -> name varchar(20)
    -> );

查询表
show tables;

插入数据 
insert into app_userinfo (name,password,age,account,create_time,depart_id,gender) values ('zs','123',12,10,'2023-05-17',1,1);
insert into app_userinfo (name,password,age,account,create_time,depart_id,gender) values ('zs2','123',12,10,'2023-05-17',1,1),('zs3','123',12,10,'2023-05-17',1,1);

查询表字段
desc app_department;


查询
select * from app_userinfo;
#!/usr/bin/env python
import pymysql

conn = pymysql.connect(             #建立和数据库的链接
    host='192.168.214.101',         #指定数据库的地址
    port=3306,                      #指定数据库的端口
    user='root',                    #链接数据库的用户
    password='tedu.cn',             #该用户的密码
    db='tedu_db',                   #默认操作的库
    charset='utf8'                  #指定字符集（可以操作中文）
)
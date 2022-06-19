import pymysql

# # 连接MySQL 创建spiders数据库
# db = pymysql.connect(host='localhost', user='root', password='aaaa', port=3306)
# cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version:', data)
# # cursor.execute('CREATE DATABASE spiders DEFAULT  CHARACTER SET utf8mb4')
# db.close()
#
# # 创建表students
# db = pymysql.connect(host='localhost', user='root', password='aaaa', port=3306, db='test')
# cursor = db.cursor()
# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL,PRIMARY KEY (id))'
# cursor = cursor.execute(sql)
# db.close()

# 插入数据
id = '20120101'
name = 'Bob'
age = 20
db = pymysql.connect(host='localhost', user='root', password='aaaa', port=3306, db='test')
cursor = db.cursor()
sql = 'INSERT INTO students(id, name , age) values(%s, %s, %s)'
try:
    cursor.execute(sql, (id, name, age))
    db.commit()
except Exception as e:
    print(e)

    db.rollback()
db.close()

# import pymysql
#
# conn = pymysql.connect(host="localhost", port=3306, user="root", password="aaaa", charset='utf8', db='test')  # 连接数据库
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 初始化游标
#
#
# id = 123
# name = 'test'
# phone = 1234567890
#
# sql = "INSERT INTO user(id,name,phone) VALUES(%s,%s,%s)"
# cursor.execute(sql, (id, name, phone))
# conn.commit()  # 提交事务
#
# cursor.close()  # 游标对象关闭
# conn.close()  # 关闭连接
print(len("12345"))
print(len(12345))

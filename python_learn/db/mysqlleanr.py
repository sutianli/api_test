import pymysql

# 1. 建立连接
conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='123456',  # password也可以
                       db='yun_bc_credit',
                       charset='utf8')  # 如果查询有中文需要指定数据库编码

# 2. 从连接建立游标（有了游标才能操作数据库）
cur = conn.cursor()

print("*******查询数据库*******")
# 3. 查询数据库（读）
cur.execute("select * from user where name='张三'")

# 4. 获取查询结果
# result = cur.fetchall()
# print(result)



# 使用cur.execute(), 执行数据库查询后无返回的是影响的行数，而非查询结果。
# 我们要使用cur.fetchone()/cur.fetchmany()/cur.fetchall()来获取查询结果
# cur.fetchone(): 获取一条数据（同时获取的数据会从结果集删除），返回元祖('张三','123456')
# cur.fetchmany(3): 获取多条数据，返回嵌套元祖(('张三','123456'),('李四','123456'),("王五","123456"))
# cur.fetchall(): 获取所有数据，返回嵌套元祖，(('张三','123456'),)（只有一条数据时）
# 注意： 获取完数据后，数据会从数据集中删除，再次获取获取不到，如：
cur.execute("select * from user")
print(cur.fetchone()) # 结果： ('张三','123456')
print(cur.fetchone()) # 结果：None
print(cur.fetchall()) # 结果：()
# 所以我们需要重复使用查询结果时，需要将查询结果赋给某个变量
cur.execute("select * from user where name='张三'")
result = cur.fetchall()
print(result)  # 结果： ('张三','123456')
print(result)  # 结果： ('张三','123456')

print("*******修改数据库*******")
# 执行修改数据库的操作后不立即生效，使用连接conn.commit()提交后才生效，支持事物及回滚
# 3. 更改数据库（写）
# cur.execute("delete from user where name='李四'")
# conn.commit()  # 4. 提交更改，注意是用的conn不是cur

# 5. 关闭游标及连接
cur.close()
conn.close()


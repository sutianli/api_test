# 获取连接方
import pymysql
from config.config import *
# 获取连接方法
def get_db_conn():
    conn=pymysql.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        passwd=db_passwd,
        db=db,
        charset='utf8')
    return  conn

# 封装数据库查询操作
def query_db(sql):
    conn = get_db_conn()  # 获取连接
    cur = conn.cursor()  # 建立游标
    logging.debug(sql)#输出执行的sql
    cur.execute(sql)  # 执行sql
    result = cur.fetchall()  # 获取所有查询结果
    logging.debug(result)#输出查询结果
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接
    return result  # 返回结果

# 封装更改数据库操作 相比用例中直接使用sql操作数据库，封装常用的数据库操作会更安全
def change_db(sql):
    conn = get_db_conn()  # 获取连接
    cur = conn.cursor()  # 建立游标
    logging.debug(sql)
    try:
        cur.execute(sql)  # 执行sql
        conn.commit()  # 提交更改
    except Exception as e:
        conn.rollback()  # 回滚
        logging.error(str(e))#输出错误信息
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接


##################try except ##########################################
# 1.捕获所有异常：
# try:
#     xxxx
# except Exception as e:
#     print(e) #打印所有异常到屏幕

# 2.捕获类型的异常
# try:
#     xxxx1
# except TypeError as e:
#     print(e) #打印类型异常到屏幕

#3.try else finally
# try:
#   xxxx1
# except:
#   xxxx2
# else:
#   xxxx3
# finally:
#   xxxx4
#   这里当xxxx1成立时就执行else下的xxxx3语句；
#   当xxxx1不成立时就执行except下的xxxx2语句
#   不管xxxx1是否成立，finally下的语句都会被执行到

# 封装常用数据库操作 相比用例中直接使用sql操作数据库，封装常用的数据库操作会更安全
def check_user(name):
    # 注意sql中''号嵌套的问题
    sql = "select * from youfenpostinfo where name = '{}'".format(name)
    result = query_db(sql)
    return True if result else False


def add_user(name, id):
    sql = "insert into youfenpostinfo (name, passwd) values ('{}','{}')".format(name, id)
    change_db(sql)


def del_user(name):
    sql = "delete from youfenpostinfo where name='{}'".format(name)
    change_db(sql)
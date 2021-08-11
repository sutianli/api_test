# 由于db.py上面这种封装方法，每一次查询都会建立一次数据库连接，效率较低，也可以采用下面面向对象的封装方法
import pymysql


class DB:
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1',
                                    port=3306,
                                    user='root',
                                    passwd='123456',  # passwd 不是 password
                                    db='api_test')
        self.cur = self.conn.cursor()

    def __del__(self):  # 析构函数，实例删除时触发
        self.cur.close()
        self.conn.close()

    def query(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def exec(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(str(e))

    def check_user(self, name):
        result = self.query("select * from user where name='{}'".format(name))
        return True if result else False

    def del_user(self, name):
        self.exec("delete from user where name='{}'".format(name))



import pymysql
from app import MYsqlDatabase, MysqlHost, MYsqlPort, MYsqlPassword, MysqlUsername


class DataBaseHandle(object):
    ''' 定义一个 MySQL 操作类'''

    def __init__(self, host, username, password, database, port):
        '''初始化数据库信息并创建数据库连接'''
        # 下面的赋值其实可以省略，connect 时 直接使用形参即可
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.port = port
        self.db = pymysql.connect(
            host=self.host,
            user=self.username,
            password=self.password,
            database=self.database,
            port=self.port,
            charset="utf8"

        )
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def insertDB(self, sql):
        ''' 插入数据库操作 '''

        try:
            # 执行sql
            self.cursor.execute(sql)

            # tt = self.cursor.execute(sql)  # 返回 插入数据 条数 可以根据 返回值 判定处理结果
            # print(tt)
            self.db.commit()

            # query = 'insert into 表名(列名1, 列名2, 列名3, 列名4, 列名5, 列名6) values(%s, %s, %s, %s, %s, %s)'
        # self.cursor.execute(sql)

        except:
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.cursor.close()

    def deleteDB(self, sql):
        ''' 操作数据库数据删除 '''

        try:
            # 执行sql
            self.cursor.execute(sql)
            # tt = self.cursor.execute(sql) # 返回 删除数据 条数 可以根据 返回值 判定处理结果
            # print(tt)
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.cursor.close()

    def updateDb(self, sql):
        ''' 更新数据库操作 '''

        try:
            # 执行sql
            self.cursor.execute(sql)
            # tt = self.cursor.execute(sql) # 返回 更新数据 条数 可以根据 返回值 判定处理结果
            # print(tt)
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.cursor.close()

    def selectDb(self, sql):
        ''' 数据库查询 '''

        try:
            self.cursor.execute(sql)  # 返回 查询数据 条数 可以根据 返回值 判定处理结果

            data = self.cursor.fetchall()  # 返回所有记录列表
            return data
        except:
            print('Error: unable to fecth data')
        finally:
            self.cursor.close()

    def closeDb(self):
        ''' 数据库连接关闭 '''
        self.db.close()


if __name__ == '__main__':
    DbHandle = DataBaseHandle(MysqlHost, MysqlUsername, MYsqlPassword, MYsqlDatabase, MYsqlPort)

    sql = "select id, mobile, username,department_name from bs_user"
    res_data = DbHandle.selectDb(sql)
    print(res_data)
    DbHandle.closeDb()

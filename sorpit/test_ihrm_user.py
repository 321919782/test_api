from api.ihrm_user import user_get_all
import unittest

from app import MysqlHost, MysqlUsername, MYsqlPassword, MYsqlDatabase, MYsqlPort
from utils import DataBaseHandle


class IhrmUserAll(unittest.TestCase):
    def test_001(self):
        # 断言数据是否正确

        # 获取get请求返回的数据
        reqeuest_data = user_get_all()

        # 去数据库查询的结果的操作
        DbHandle = DataBaseHandle(MysqlHost, MysqlUsername, MYsqlPassword, MYsqlDatabase, MYsqlPort)
        sql = "select id,mobile,username,department_name from bs_user where company_id=1"
        Mysql_data = DbHandle.selectDb(sql)
        DbHandle.closeDb()

        rquests_number = reqeuest_data["data"]["total"]

        mysql_number = len(Mysql_data)
        self.assertEqual(rquests_number, mysql_number)

import json
import unittest, parameterized

from api.yun_login import yun_login_api
from app import BSEE_DIR
from utils import DataBaseHandle
from app import MysqlHost,MYsqlPort,MYsqlDatabase,MYsqlPassword,MysqlUsername

def build_data():
    # 准备JSON数据的路径
    str_path = BSEE_DIR + "/data/user_pwd.json"
    print(str_path)

    # 打开文件获取数据
    with open(str_path, "r") as f:
        res = f.read()
        print(type(res))
        dic_res = json.loads(res)
    list = []

    # 组装数据
    for i in dic_res["data"]:
        tupe = (i["username"], i["password"], i["code"])
        list.append(tupe)
    return list


class YunLoginTest(unittest.TestCase):
    # def test_001(self):
    #     # 准备请求数据和断言0
    #     username = "peter"
    #     password = "admin"
    #     code = 200
    #
    #     # 获取request是请求以后的JSON数据
    #     json_data = yun_login_api(username, password)
    #     self.assertEqual(int(json_data["result"]), code)
    #
    # # 错误密码的数据断言
    # def test_002(self):
    #     def test_001(self):
    #         # 准备请求数据和断言
    #         username = "peter"
    #         password = "admin1"
    #         code = 200
    #
    #         # 获取request是请求以后的JSON数据
    #         json_data = yun_login_api(username, password)
    #         self.assertEqual(int(json_data["result"]), code)
    @parameterized.parameterized.expand([('peter','admin',200),('peter1',"admin",5),('peter','admin1',4)])
    def test_001(self,username,password,code):

        json_data = yun_login_api(username,password)

        self.assertEqual(int(json_data['result']),code)










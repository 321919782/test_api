import unittest
import datetime

from app import BSEE_DIR
from sorpit.test_yun_login import YunLoginTest
from tools.HTMLTestRunner import HTMLTestRunner
from sorpit.test_ihrm_user import IhrmUserAll

# 加载case到套件里


suite = unittest.TestSuite()
# suite.addTest(unittest.makeSuite(YunLoginTest))
suite.addTest(unittest.makeSuite(IhrmUserAll))

# 执行套件，生成测试报告

# 打开文件，来写入测试用例

# 时间类型的数据 type=datetime.datetime
data_time = datetime.datetime.now()
str_datatime = datetime.datetime.strftime(data_time, '%Y%m%d%H%M%S')
print(str_datatime)

report_path = BSEE_DIR + "./report/yun_login_test--%s.html" % str_datatime

f = open(report_path, "wb")
# 指定HTMLTestRun而的参数
runner = HTMLTestRunner(stream=f, title="Yun系统登录接口报告", description="Chrome 浏览器")
# 执行并生成报告
runner.run(suite)

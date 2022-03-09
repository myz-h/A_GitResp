"""
Author:sick
DateTime:2022/2/10 20:28
# type:openpyxl.workbook.workbook.Worksheet
# Email:goqsqulatiimdeai
"""
import os
import time
import unittest

# unittest 驱动
import ddt
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver

from Auto_Deom.Auto_selenium.com.bw.deom.pages.loginpage import LoginPage


@ddt.ddt
class LoginCase(unittest.TestCase):
    # 测试夹
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.url = "http://localhost:8080/shop1/login.action"

    @ddt.file_data("../data/login_test.yaml")
    def test_login(self, username, password, yzm, result):
        # 实列化loginpage
        pagel = LoginPage(self.driver, self.url)
        #访问url
        pagel.open_get()
        #输入用户名
        pagel.input_username_m(username)
        #输入密码
        pagel.input_password_m(password)
        #输入验证码
        pagel.input_yzm_m(yzm)
        #点击复选框
        pagel.clickcheck()
        #点击提交
        pagel.button_submit_m()
        #休眠5秒
        time.sleep(5)
        #断言
        self.assertEqual(pagel.getTitle(),result)
    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    #获取文件的绝对路径
    report_path=os.path.dirname(os.path.realpath(__file__))
    #获取测试报告路径
    report_abspath=os.path.join(r"E:\developer\pycharm_workspace\pythonProject_auto\Auto_Deom\Auto_selenium\com\bw\deom\report","result.html")
    #获取文件
    fp=open(file=report_abspath,mode="wb")
    #报告详情
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="自动化测试报告",description="用例执行情况")
    #实例化
    testsuite=unittest.TestSuite()
    #加载用例
    # loadTestsFromTestCase()中放入类
    # loadTestsFromModule()中放入模块 .py
    # loadTestsFromName()中放入 模块名.类名.testcase名
    testsuite.addTests(unittest.TestLoader().loadTestsFromTestCase(LoginCase))
    runner.run(testsuite)
    fp.close()
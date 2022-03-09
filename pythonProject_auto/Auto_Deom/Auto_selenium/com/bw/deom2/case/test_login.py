"""
Author:sick
DateTime:2022/2/11 20:26
# type:openpyxl.workbook.workbook.Worksheet
# Email:goqsqulatiimdeai
"""
import os
import time
import unittest

import ddt
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver

from Auto_Deom.Auto_selenium.com.bw.deom2.pages.loginpages import LoginPages

"""
封装case
"""

@ddt.ddt
class LogingCase(unittest.TestCase):
    # 运行前准备
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.url = "http://localhost:8080/shop1/login.action"

    # case
    @ddt.file_data("../data/test_login.yaml")
    def test_logincase(self, username, password, captcha,result):
        # 实例化LoginPages
        lp = LoginPages(self.driver, self.url)
        #打开web
        lp.open()
        #编译
        lp.sendUsername(username)
        lp.sendPassword(password)
        lp.sendCaptcha(captcha)
        #点击记住密码
        lp.checkout_m()
        #点击登录
        lp.sub_m()
        #断言
        self.assertEqual(lp.getTitle(),result)
    # 在方法之后
    def tearDown(self) -> None:
        time.sleep(5)
        self.driver.quit()
if __name__ == '__main__':
    #获取文件的绝对路径
    report_path=os.path.dirname(os.path.realpath(__file__))
    #获取测试报告路径
    report_abspath=os.path.join(r"E:\developer\pycharm_workspace\pythonProject_auto\Auto_Deom\Auto_selenium\com\bw\deom2\report","login.html")
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
    testsuite.addTests(unittest.TestLoader().loadTestsFromTestCase(LogingCase))
    runner.run(testsuite)
    fp.close()

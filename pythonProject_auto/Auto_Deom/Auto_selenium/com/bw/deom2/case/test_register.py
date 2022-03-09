"""
Author:sick
DateTime:2022/2/11 20:27
# type:openpyxl.workbook.workbook.Worksheet
# Email:goqsqulatiimdeai
"""
import os
import time
import unittest

import ddt
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver

from Auto_Deom.Auto_selenium.com.bw.deom2.pages.registerpages import RegisterPages


@ddt.ddt
class RegsiterCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome()
        self.url="http://localhost:8080/shop1/regist.action"
    @ddt.file_data("../data/test_register.yaml")
    def test_register(self,username,password,repassword,email,name,phone,address,captcha,result):
        #实例化registerpages.py
        regs=RegisterPages(self.driver,self.url)
        #打开web
        regs.open()
        time.sleep(3)
        regs.rusername_m(username)
        regs.rpassword_m(password)
        regs.rrepassword_m(repassword)
        regs.reamil_m(email)
        regs.rname_m(name)
        regs.rphone_m(phone)
        regs.raddress_m(address)
        regs.rcaptcha_m(captcha)
        #点击
        regs.submit_reg_m()
        #断言
        self.assertEqual(regs.getTitle(),result)
    def tearDown(self) -> None:
        time.sleep(5)
        self.driver.quit()


if __name__ == '__main__':
    #获取文件的绝对路径
    report_path=os.path.dirname(os.path.realpath(__file__))
    #获取测试报告路径
    report_abspath=os.path.join(r"E:\developer\pycharm_workspace\pythonProject_auto\Auto_Deom\Auto_selenium\com\bw\deom2\report","register.html")
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
    testsuite.addTests(unittest.TestLoader().loadTestsFromTestCase(RegsiterCase))
    # testsuite.addTests(unittest.TestLoader().loadTestsFromModule(RegsiterCase))
    runner.run(testsuite)
    fp.close()

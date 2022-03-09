"""
Author:sick
DateTime:2022/2/10 14:18
# type:openpyxl.workbook.workbook.Worksheet
# Email:goqsqulatiimdeai
"""
import os
import unittest

from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    #获取文件的绝对路径1
    report_path=os.path.dirname(os.path.realpath(__file__))
    #获取测试报告路径
    report_abspath=os.path.join(report_path,"result.html")
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
    testsuite.addTests(unittest.TestLoader().loadTestsFromTestCase())
    runner.run(testsuite)
    fp.close()

if __name__ == '__main__':
    #获取执行位置
    tests = unittest.defaultTestLoader.discover(r"com/bw/deom", "*.py")
    #创建HTML位置 二进制
    s = open(os.getcwd() + "/a.html", "wb")
    #调用HTMLTestRunner
    r = HTMLTestRunner.HTMLTestRunner(stream=s, verbosity=0, title="辉煌八维大数据", description="666")
    r.run(tests)
    # 释放资源
    s.close()
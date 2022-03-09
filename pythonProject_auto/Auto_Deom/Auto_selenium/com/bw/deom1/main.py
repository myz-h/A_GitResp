"""
Author:sick
DateTime:2022/2/11 19:08
# type:openpyxl.workbook.workbook.Worksheet
# Email:goqsqulatiimdeai
"""
import os
import unittest

from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    # print(os.getcwd())
    # 获取执行位置
    tests = unittest.defaultTestLoader.discover(os.getcwd()+"/case", "*.py")
    # 创建HTML位置 二进制
    s = open(os.getcwd() + "/report/result.html", "wb")
    # 调用HTMLTestRunner
    r = HTMLTestRunner.HTMLTestRunner(stream=s, verbosity=2, title="辉煌八维大数据", description="666")
    r.run(tests)
    # 释放资源
    s.close()
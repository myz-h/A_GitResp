"""
Author:sick
DateTime:2022/2/9 19:04
# type:openpyxl.workbook.workbook.Worksheet
# Email:goqsqulatiimdeai
# loadTestsFromTestCase(testCaseClass)
# testCaseClass必须是TestCase的子类（或孙类也行）
# loadTestsFromModule(module, pattern=None)
# test case所在的module
# loadTestsFromName(name, module=None)
# name是一个string，string需要是是这种格式的“module.class.method”
# loadTestsFromNames(name, module=None)
# names是一个list，用法与上同
# discover(start_dir, pattern=’test*.py’, top_level_dir=None)
# 从python文件中获取test case
"""
import os
import unittest

from HTMLTestRunner import HTMLTestRunner
# print(os.getcwd())
if __name__ == '__main__':
    # print(os.getcwd())
    #获取执行位置
    tests = unittest.defaultTestLoader.discover(r"com/bw/deom1", "*.py")
    #创建HTML位置 二进制
    s = open(os.getcwd() + "/a.html", "wb")
    #调用HTMLTestRunner
    r = HTMLTestRunner.HTMLTestRunner(stream=s, verbosity=0, title="辉煌八维大数据", description="666")
    r.run(tests)
    # 释放资源
    s.close()
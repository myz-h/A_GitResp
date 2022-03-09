"""
Author:sick
DateTime:2022/2/9 18:44
# type:openpyxl.workbook.workbook.Worksheet
# Email:goqsqulatiimdeai
"""
import os
import unittest

from HTMLTestRunner import HTMLTestRunner


class TestDeom_1(unittest.TestCase):

    def setUp(self) -> None:
        print("方法之前运行")

    @classmethod
    def setUpClass(cls) -> None:
        print("类之前运行")

    @unittest.skipIf(10 > 20, "10>20")
    def test01(self):
        print("1231111111111111")

    @unittest.skip("跳过")
    def test02(self):
        print("4562222222222222222")

    @unittest.skipUnless(10 < 20, "10<20")
    def test03(self):
        print("789")

    def test04(self):
        print("7899999999")
        self.assertEqual(1,2)

    def test05(self):
        print("我是沈爸爸")

    def tearDown(self) -> None:
        print("方法之后运行")

    @classmethod
    def tearDownClass(cls) -> None:
        print("类之后运行")

# if __name__ == '__main__':
    #     # 指定运行执行
    #     unittest.main(defaultTest="TestDeom_1.test01")
    #     suite=unittest.TestSuite()
    #     suite.addTest(test=TestDeom_1("test01"))
    #     suite.addTest(test=TestDeom_1("test02"))
    #     # #第一种运行套件
    #     unittest.main(defaultTest="suite")
    #     # unittest.TextTestRunner().run(suite)
if __name__ == '__main__':
        # 当前文件夹路径
        # E:\developer\pycharm_workspace\pythonProject_auto\Auto_Deom\Deom_1\com\bw\deom
        # E:\developer\pycharm_workspace\pythonProject_auto\Auto_Deom\Deom_1\com\bw\deom\result.html
        report_path = os.path.dirname(os.path.realpath(__file__))
        # 测试报告地址
        report_abspath = os.path.join(report_path, "result.html")
        fp = open(report_abspath, "wb")
        # 报告详情
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                                  title=u'自动化测试报告,测试结果如下：',
                                                  description=u'用例执行情况：')
        # 实例化
        testunit = unittest.TestSuite()
        # 加载用例
        testunit.addTests(unittest.TestLoader().loadTestsFromTestCase(TestDeom_1))
        # 执行用例
        runner.run(testunit)
        # 关闭报告
        fp.close()
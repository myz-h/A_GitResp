"""
Author:sick
DateTime:2022/2/9 18:44
# type:openpyxl.workbook.workbook.Worksheet
# Email:goqsqulatiimdeai
"""
import unittest


class TestDeom_1(unittest.TestCase):

    def setUp(self) -> None:
        print("方法之前运行")

    @classmethod
    def setUpClass(cls) -> None:
        print("类之前运行")

    def test01(self):
        print("1231111111111111")

    def test02(self):
        print("4562222222222222222")

    def test03(self):
        print("789")

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
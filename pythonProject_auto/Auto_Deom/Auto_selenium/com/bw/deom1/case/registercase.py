"""
Author:sick
DateTime:2022/2/11 16:34
# type:openpyxl.workbook.workbook.Worksheet
# Email:goqsqulatiimdeai
"""
import os
import time
import unittest

import ddt
from selenium import webdriver

from Auto_Deom.Auto_selenium.com.bw.deom1.pages.registpages import RegistPage


@ddt.ddt
class RegisterCase(unittest.TestCase):

    # 初始化setup
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.url = "http://localhost:8080/shop1/regist.action"

    # 注册测试用例
    @ddt.file_data(r"E:\developer\pycharm_workspace\pythonProject_auto\Auto_Deom\Auto_selenium\com\bw\deom1\data\regsiter.yaml")
    def test_register(self, username, password, repasswrod, email, name, phone, addr, captcha, result):
        # 实例化注册
        res = RegistPage(self.driver, self.url)
        # # 获取页面路径
        res.open()
        # 调用
        res.input_username_m(username)
        res.input_password_m(password)
        res.input_repassword_m(repasswrod)
        res.input_eamil_m(email)
        res.input_name_m(name)
        res.input_phone_m(phone)
        res.input_addr_m(addr)
        res.input_captcha_m(captcha)
        # 点击
        res.button_sub_m()
        # #断言
        self.assertEqual(res.getTitle(), result)
    # 初始化teardown
    def tearDown(self) -> None:
        time.sleep(5)
        self.driver.quit()
# if __name__ == '__main__':
#     unittest.main()

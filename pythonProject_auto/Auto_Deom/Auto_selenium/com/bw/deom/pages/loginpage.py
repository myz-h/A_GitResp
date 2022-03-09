"""
Author:sick
DateTime:2022/2/10 19:38
# type:openpyxl.workbook.workbook.Worksheet
# Email:goqsqulatiimdeai
"""
from selenium.webdriver.common.by import By

from Auto_Deom.Auto_selenium.com.bw.deom.basepage.basepage import BasePage


class LoginPage(BasePage):
    # 输入框进行
    input_username = (By.ID,"username")
    input_password = (By.ID,"password")
    input_yzm = (By.ID,"captcha")
    check_rusername = (By.ID,"isRememberUsername")
    button_submit = (By.CLASS_NAME,"submit")
    #初始化构造器
    def __init__(self,driver,url):
        #初始化父类构造器
        BasePage.__init__(self=self,driver=driver,url=url)
    """
        封装用户行为
    """
    #输入用户名
    def input_username_m(self,name):
        self.sendValue(self.input_username,name)
    #输入密码
    def input_password_m(self,password):
        self.sendValue(self.input_password,password)
    #输入验证码
    def input_yzm_m(self,yzm):
        self.sendValue(self.input_yzm,yzm)
    #点击复选框
    def clickcheck(self):
        self.click_m(self.check_rusername)
    #点击提交按钮
    def button_submit_m(self):
        self.click_m(self.button_submit)
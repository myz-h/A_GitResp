"""
Author:sick
DateTime:2022/2/11 20:28
# type:openpyxl.workbook.workbook.Worksheet
# Email:goqsqulatiimdeai
"""
from selenium.webdriver.common.by import By

from Auto_Deom.Auto_selenium.com.bw.deom2.basepage.basepage import BasePage

"""
封装登录类
"""
class LoginPages(BasePage):
    #初始化父类构造器
    def __init__(self,driver,url):
        #父类实例化
        BasePage.__init__(self,driver,url)
    #获取类型
    #编译值
    username_m=(By.ID,"username")
    password_m=(By.ID,"password")
    captcha_m=(By.ID,"captcha")
    checkbox_m=(By.ID,"isRememberUsername")
    submit_m=(By.CLASS_NAME,"submit")

    #
    #封装用户行为
    #写入username
    def sendUsername(self,username):
        self.sendVal(loc=self.username_m,val=username)
    def sendPassword(self,password):
        self.sendVal(loc=self.password_m,val=password)
    def sendCaptcha(self,captcha):
        self.sendVal(loc=self.captcha_m,val=captcha)
    #点击check
    def checkout_m(self):
        self.click_but(loc=self.checkbox_m)
    #点击登录按钮
    def sub_m(self):
        self.click_but(loc=self.submit_m)
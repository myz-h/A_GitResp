"""
Author:sick
DateTime:2022/2/11 16:07
# type:openpyxl.workbook.workbook.Worksheet
# Email:goqsqulatiimdeai
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


#
from Auto_Deom.Auto_selenium.com.bw.deom1.basepage.basepage import BasePage


class RegistPage(BasePage):
    """
        编译值
        """
    # 输入框
    input_username = (By.ID, "username")
    input_password = (By.ID, "password")
    input_repassword = (By.ID, "rePassword")
    input_eamil = (By.ID, "email")
    input_name = (By.NAME, "name")
    input_phone = (By.NAME, "phone")
    input_addr = (By.NAME, "addr")
    input_captcha = (By.ID, "captcha")
    #注册按钮
    button_sub=(By.CLASS_NAME,"submit")
    #初始化父类驱动
    def __init__(self,driver,url):
        #实列化父类
        BasePage.__init__(self,driver,url)

    #封装行为
    #写入username
    def input_username_m(self,username):
        self.sendValue(loc=self.input_username,val=username)
    # 写入password
    def input_password_m(self,password):
        self.sendValue(loc=self.input_password,val=password)
    # 再次确认密码
    def input_repassword_m(self,rePassword):
        self.sendValue(loc=self.input_repassword,val=rePassword)
    # 写入email
    def input_eamil_m(self,email):
        self.sendValue(loc=self.input_eamil,val=email)
    # 写入name
    def input_name_m(self,name):
        self.sendValue(loc=self.input_name,val=name)
    # 写入phone
    def input_phone_m(self,phone):
        self.sendValue(loc=self.input_phone,val=phone)
    # 写入address
    def input_addr_m(self,addr):
        self.sendValue(loc=self.input_addr,val=addr)
    # 写入验证码
    def input_captcha_m(self,captcha):
        self.sendValue(loc=self.input_captcha,val=captcha)
    #点击注册按钮
    def button_sub_m(self):
        self.click_check(loc=self.button_sub)

# if __name__ == '__main__':
#     rp=RegistPage(driver = webdriver.Chrome(),url = "http://localhost:8080/shop1/regist.action")
#     rp.open()
#     rp.input_name_m(name="456")
#     time.sleep(5)
#     print(rp.getTitle())
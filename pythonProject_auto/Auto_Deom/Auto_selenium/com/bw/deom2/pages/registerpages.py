"""
Author:sick
DateTime:2022/2/11 20:28
# type:openpyxl.workbook.workbook.Worksheet
# Email:goqsqulatiimdeai
"""
from selenium.webdriver.common.by import By

from Auto_Deom.Auto_selenium.com.bw.deom2.basepage.basepage import BasePage

"""
封装注册行为
"""
class RegisterPages(BasePage):
    #初始化父类构造器
    def __init__(self,driver,url):
        BasePage.__init__(self,driver,url)
    #编译类型
    username_m=(By.ID,"username")
    password_m=(By.ID,"password")
    repassword_m=(By.ID,"rePassword")
    email_m=(By.ID,"email")
    name_m=(By.NAME,"name")
    phone_m=(By.NAME,"phone")
    address_m=(By.NAME,"addr")
    captcha_m=(By.ID,"captcha")
    but_submit_m=(By.CLASS_NAME,"submit")
    #封装用户行为
    def rusername_m(self,username):
        self.sendVal(loc=self.username_m,val=username)
    def rpassword_m(self,password):
        self.sendVal(loc=self.password_m,val=password)
    def rrepassword_m(self,repassword):
        self.sendVal(loc=self.repassword_m,val=repassword)
    def reamil_m(self,email):
        self.sendVal(loc=self.email_m,val=email)
    def rname_m(self,name):
        self.sendVal(loc=self.name_m,val=name)
    def rphone_m(self,phone):
        self.sendVal(loc=self.phone_m,val=phone)
    def raddress_m(self,address):
        self.sendVal(loc=self.address_m,val=address)
    def rcaptcha_m(self,captcha):
        self.sendVal(loc=self.captcha_m,val=captcha)
    #点击提交
    def submit_reg_m(self):
        self.click_but(self.but_submit_m)
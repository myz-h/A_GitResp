"""
Author:sick
DateTime:2022/2/11 20:27
# type:openpyxl.workbook.workbook.Worksheet
# Email:goqsqulatiimdeai
"""
from selenium import webdriver

"""
针对selenium进行二次封装
"""


class BasePage():
    # 初始化构造器 driver web驱动 url web地址
    def __init__(self, driver=webdriver.Chrome(), url="http://localhost:8080/shop1/login.action"):
        # 赋值操作
        self.driver = driver
        self.url = url
        # 页面等待10秒
        self.driver.implicitly_wait(10)

    # 封装selenium方法
    # 打开web地址
    def open(self):
        self.driver.get(self.url)

    # 定位单元素 loc == (By..,"p1")
    def findElement(self, loc):
        # 调用驱动方法
        return self.driver.find_element(*loc)

    # 定位多元素
    def findElements(self, loc):
        # 调用驱动方法
        return self.driver.find_elements(*loc)

    # 发送内容
    def sendVal(self, loc, val):
        self.findElement(loc).send_keys(val)

    # 点击按钮
    def click_but(self, loc):
        self.findElement(loc).click()

    # 获取标题
    def getTitle(self):
        return self.driver.title

    # 获取text
    def getText(self, loc):
        return self.findElement(loc).text
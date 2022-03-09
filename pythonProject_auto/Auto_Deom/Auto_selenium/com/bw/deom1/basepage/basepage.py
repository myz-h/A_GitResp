"""
Author:sick
DateTime:2022/2/11 14:08
# type:openpyxl.workbook.workbook.Worksheet
# Email:goqsqulatiimdeai
"""
from selenium import webdriver


class BasePage():
    #初始化构造器
    def __init__(self,driver,url):
        self.driver=driver
        self.url=url
        self.driver.implicitly_wait(30)
    """
    封装selenium原生操作
    """
    #获取路径
    def open(self):
        #
        self.driver.get(self.url)
    #获取元素
    def findElement(self,loc):
        return self.driver.find_element(*loc)
    #获取多个元素
    def findElements(self,loc):
        return self.driver.find_elements(*loc)
    #写入内容
    def sendValue(self,loc,val):
        self.findElement(loc).send_keys(val)
    #点击
    def click_check(self,loc):
        self.findElement(loc).click()
    #获取标头
    def getTitle(self):
        return self.driver.title
    #获取文本
    def getText(self,loc):
        return self.findElement(loc).text

# if __name__ == '__main__':
#     d = BasePage()
#     d.open()

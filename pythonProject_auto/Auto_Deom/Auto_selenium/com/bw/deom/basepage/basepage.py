"""
Author:sick
DateTime:2022/2/10 18:37
# type:openpyxl.workbook.workbook.Worksheet
# Email:goqsqulatiimdeai
"""
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get()
# driver.implicitly_wait()
# s1=driver.find_element()
# s1.get_attribute()
# s=driver.find_elements()
from selenium import webdriver


class BasePage():
    """
    封装selenium常用的操作
    """
    #初始化构造器 驱动driver url
    def __init__(self,driver,url):
        #初始化driver
        self.driver = driver
        #初始化路径
        self.url = url
        #等待10
        self.driver.implicitly_wait(10)
    #获取页面路径
    def open_get(self):
        #driver.get(url=self.url)
        self.driver.get(self.url)
    #查询单个元素 loc==>(By.ID、NAME,"元素标识符")
    def find_Element(self,loc):
        #*loc等于解包==>by=By.id,value="p1"
        return self.driver.find_element(*loc)
    #查询多个元素
    def find_Elements(self,loc):
        #
        return self.driver.find_elements(*loc)
    #点击按钮
    def click_m(self,loc):
        #调用查询单个元素后进行点击
        self.find_Element(loc).click()
    #发送内容
    def sendValue(self,loc,value):
        #先定位到位置、在进行赋值操作
        self.find_Element(loc).send_keys(value)
    #获取元素属性
    def getattr(self,loc,attrName):
        #先定位元素，在进行获取值
        return self.find_Element(loc).get_attribute(attrName)
    #获取文本
    def getText(self,loc):
        return self.find_Element(loc).text
    #获取标题
    def getTitle(self):
        return self.driver.title
# if __name__ == '__main__':
#     bp=BasePage(driver=webdriver.Chrome(),url="https://www.zhihu.com/question/waiting")
#     bp.open_get()
#     print(bp.getTitle())
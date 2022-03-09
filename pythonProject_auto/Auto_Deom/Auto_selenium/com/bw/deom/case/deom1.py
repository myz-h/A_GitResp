"""
Author:sick
DateTime:2022/2/10 19:00
# type:openpyxl.workbook.workbook.Worksheet
# Email:goqsqulatiimdeai
"""
import os
import unittest


from Auto_Deom.Auto_selenium.com.bw.deom.basepage.basepage import BasePage

if __name__ == '__main__':
    print(os.getcwd())
    print(os.path.abspath("login_test.yaml"))
    print(os.path.realpath(__file__))
    # print(os.path.dirname("login_test.yaml"))
    print(os.path.dirname(os.path.realpath(__file__)))
    # print(os.getenv)
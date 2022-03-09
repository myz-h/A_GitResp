"""
Author:sick
DateTime:2022/2/17 20:04
# type:openpyxl.workbook.workbook.Worksheet
# Email:goqsqulatiimdeai
"""
import random
import string

total = string.ascii_letters + string.digits + string.punctuation
length = 16
password = "".join(random.sample(total, length))
print(password)
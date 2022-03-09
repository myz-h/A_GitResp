"""
Author:sick
DateTime:2022/2/17 18:45
# type:openpyxl.workbook.workbook.Worksheet
# Email:goqsqulatiimdeai
"""
import json


# def Json2Csv(filename):
#     try:
#         with open(file=filename, mode="r", encoding="utf-8") as f:
#             data = json.loads(f.read())
#
if __name__ == '__main__':
    try:
        with open(file='data/input.json',mode='r') as f:
            data = json.loads(f.read())
        # output=Name,age,birthyear
        output = ','.join([*data[0]])
        # dict1 = {"obj": "world", "name": "python"}
        # print("hello {names[obj]}, this is {names[name]}.".format(names=dict1))
        # {'Name': 'Akash', 'age': 26, 'birthyear': '1994'}
        for obj in data:
            # output += '{obj["Name"]},{obj["age"]},{obj["birthyear"]}'.format(obj=[*data])
             output += '\n'+'{names[Name]},{names[age]},{names[birthyear]}'.format(names=obj)
            # output += f'\n{obj["Name"]},{obj["age"]},{obj["birthyear"]}'
            # print('{obj[0]},{obj[1]},{obj[2]}'.format(data))
            # print(output)
            # print(output)
        # print(output)
        with open(file="data/output.csv",mode="w") as f:
            f.write(output)
    except Exception as ex:
        print(f'Error:{str(ex)}')

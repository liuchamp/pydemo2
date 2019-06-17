# -*- coding: utf-8 -*
scores = {'语文': 89, '数学': 92, '英语': 93}
print(scores)
# 空的花括号代表空的dict
empty_dict = {}
print(empty_dict)
# 使用元组作为dict的key
dict2 = {(20, 30): 'good', 30: 'bad'}
print(dict2)

vegetables = [('celery', 1.58), ('brocoli', 1.29), ('lettuce', 2.19)]
# 创建包含3组key-value对的字典
dict3 = dict(vegetables)
print(dict3)  # {'celery': 1.58, 'brocoli': 1.29, 'lettuce': 2.19}
cars = [['BMW', 8.5], ['BENS', 8.3], ['AUDI', 7.9]]
# 创建包含3组key-value对的字典
dict4 = dict(cars)
print(dict4)  # {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}

# -*- coding: utf-8 -*

# 列表和元组可以和整数执行乘法运算，列表和元组乘法的意义就是把它们包含的元素重复 N 次（N 就是被乘的倍数）。
a_tuple = ('crazyit', 20)
# 执行乘法
mul_tuple = a_tuple * 3
print(mul_tuple)  # ('crazyit', 20, 'crazyit', 20, 'crazyit', 20)
a_list = [30, 'Python', 2]
mul_list = a_list * 3
print(mul_list)  # [30, 'Python', 2, 30, 'Python', 2, 30, 'Python', 2]


# n 运算符用于判断列表或元组是否包含某个元素，例如如下代码：

a_tuple = ('crazyit', 20, -1.2)
print(20 in a_tuple)  # True
print(1.2 in a_tuple)  # False
print('fkit' not in a_tuple)  # True


# Python 提供了内置的 ten()、max()、min() 全局函数来获取元组或列表的长度、最大值和最小值。

# 元素都是数值的元组
a_tuple = (20, 10, -2, 15.2, 102, 50)
# 计算最大值
print(max(a_tuple))  # 102
# 计算最小值
print(min(a_tuple))  # -2
# 计算长度
print(len(a_tuple))  # 6
# 元素都是字符串的列表
b_list = ['crazyit', 'fkit', 'Python', 'Kotlin']
# 计算最大值（依次比较每个字符的ASCII码值，先比较第一个字符，若相同，继续比较第二个字符，以此类推）
print(max(b_list))  # fkit（26个小写字母的ASCII码为97~122）
# 计算最小值
print(min(b_list))  # Kotlin （26个大写字母的ASCII码为65~90）
# 计算长度
print(len(b_list))  # 4


# 序列封包和序列解包
a_list = ['crazyit', 20, -2]
# 追加元素
a_list.append('fkit')
print(a_list)  # ['crazyit', 20, -2, 'fkit']
a_tuple = (3.4, 5.6)
# 追加元组，元组被当成一个元素
a_list.append(a_tuple)
print(a_list)  # ['crazyit', 20, -2, 'fkit', (3.4, 5.6)]
# 追加列表，列表被当成一个元素
a_list.append(['a', 'b'])
print(a_list)  # ['crazyit', 20, -2, 'fkit', (3.4, 5.6), ['a', 'b']]

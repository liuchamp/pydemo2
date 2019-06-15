# -*- coding: utf-8 -*

a_list = [2, 30, 'a', [5, 30], 30]
# 计算列表中30的出现次数
print(a_list.count(30))  # 2
# 计算列表中[5, 30]的出现次数
print(a_list.count([5, 30]))  # 1


a_list = [2, 30, 'a', 'b', 'crazyit', 30]
# 定位元素30的出现位置
print(a_list.index(30))  # 1
# 从索引2处开始、定位元素30的出现位置
print(a_list.index(30, 2))  # 5
# 从索引2处到索引4处之间定位元素30的出现位置，找不到该元素
# print(a_list.index(30, 2, 4))  # ValueError


stack = []
# 向栈中“入栈”3个元素
stack.append("fkit")
stack.append("crazyit")
stack.append("Charlie")
print(stack)  # ['fkit', 'crazyit', 'Charlie']
# 第一次出栈：最后入栈的元素被移出栈
print(stack.pop())
print(stack)  # ['fkit', 'crazyit']
# 再次出栈
print(stack.pop())
print(stack)  # ['fkit']

a_list = list(range(1, 8))
# 将a_list列表元素反转
a_list.reverse()
print(a_list)  # [7, 6, 5, 4, 3, 2, 1]


a_list = [3, 4, -2, -30, 14, 9.3, 3.4]
# 对列表元素排序
a_list.sort()
print(a_list)  # [-30, -2, 3, 3.4, 4, 9.3, 14]
b_list = ['Python', 'Swift', 'Ruby', 'Go', 'Kotlin', 'Erlang']
# 对列表元素排序：默认按字符串包含的字符的编码大小比较
b_list.sort()
print(b_list)  # ['Erlang', 'Go', 'Kotlin', 'Python', 'Ruby', 'Swift']


# 以下代码只能在Python 2.x中执行
# 定义一个根据长度比较大小的比较函数
def len_cmp(x, y):
    # 下面代码比较大小的逻辑是：长度大的字符串就算更大
    return 1 if len(x) > len(y) else (-1 if len(x) < len(y) else 0)


b_list.sort(len_cmp)
print(b_list)  # ['Go', 'Ruby', 'Swift', 'Erlang', 'Kotlin', 'Python']

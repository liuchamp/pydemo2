# -*- coding: utf-8 -*

price = 108
print("the book's price is %s" % price)


user = "Charli"
age = 8
# 格式化字符串有两个占位符，第三部分提供2个变量
print("%s is a %s years old boy" % (user, age))


num = -28
print("num is: %6i" % num)
print("num is: %6d" % num)
print("num is: %6o" % num)
print("num is: %6x" % num)
print("num is: %6X" % num)
print("num is: %6s" % num)


s = 'crazyit.org is very good'
# 获取s中索引2处的字符
print(s[2])  # 输出a
# 获取s中从右边开始，索引4处的字符
print(s[-4])  # 输出g

# 获取s中从索引3处到索引5处（不包含）的子串
print(s[3: 5])  # 输出zy
# 获取s中从索引3处到倒数第5个字符的子串
print(s[3: -5])  # 输出zyit.org is very
# 获取s中从倒数第6个字符到倒数第3个字符的子串
print(s[-6: -3])  # 输出y g

# 获取s中从索引5处到结束的子串
print(s[5:])  # 输出it.org is very good
# 获取s中从倒数第6个字符到结束的子串
print(s[-6:])  # 输出y good
# 获取s中从开始到索引5处的子串
print(s[: 5])  # 输出crazy
# 获取s中从开始到倒数第6个字符的子串
print(s[: -6])  # 输出crazyit.org is ver

# 判断s是否包含'very'子串
print('very' in s)  # True
print('fkit' in s)  # False


# 输出s的长度
print(len(s))  # 24
# 输出'test'的长度
print(len('test'))  # 4

# 输出s字符串中最大的字符
print(max(s))  # z
# 输出s字符串中最大的字符
print(min(s))  # 空格

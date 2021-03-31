'''
计算字符串的长度
str1 = '我是中华人民共和国的接班人'
print(len(str1))

截取字符串的写法
str1 = '我是中华人民共和国的接班人'
str2 = str1[0:5]
打印：我是中华人

分割字符串
str1 = '我是中华人民共和国的接班人中华人的'
list = str1.split('中华人',1)
print(list)
打印：['我是', '民共和国的接班人中华人的']

字符串的startswith方法
str1 = '我是中华人民共和国的接班人中华人的'
b = str1.startswith('我是')
print(b)

字母大小写
str1 = 'abcd'
str1 = str1.upper()
print(str1)

str1 = 'ABCD'
str1 = str1.lower()
print(str1)

字符串去除左右两边的空格或者特殊字符(不能去除中间的)
str.strip()
字符串去除左边的空格或者特殊字符(不能去除中间的)
str.lstrip()
字符串去除右边的空格或者特殊字符(不能去除中间的)
str.rstrip()

'''

str1 = 'tABtCDt'
str1=str1.lstrip('t')
print(str1)

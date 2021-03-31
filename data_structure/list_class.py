'''

定义一个空列表
list1=[]

遍历一个列表
list1 = ['南京', '天津', '北京', '上海']
for item in list1:
    print(item)

遍历一个列表，并且可以获取每个值的索引
list1 = ['南京', '天津', '北京', '上海']
for index, item in enumerate(list1):
    print('当前索引为', index, '值为', item)

根据一个索引获取一个值
list1 = ['南京', '天津', '北京', '上海']
var = list1[0]
print(var)

添加一个元素到列表中去（类似于java中的add方法）
list1 = ['南京', '天津', '北京', '上海']
list1.append('信阳')
print(list1)

把一个列表添加到另一个列表中去（类似于java中的addAll方法） (不会去重)
list1 = ['南京', '天津', '北京', '上海']
list2 = ['北平', '深圳', '北京', '广州']
list1.extend(list2)
print(list1)

删除某个元素（通过索引删除）
list1 = ['南京', '天津', '北京', '上海']
del list1[0]
print(list1)

删除某个元素，直接通过值删除
list1 = ['南京', '天津', '北京', '上海']
# list.count方法判断该值在列表中出现的次数
count = list1.count('南京')
if count > 0:
    list1.remove('南京')
else:
    print('该值不存在')

获取某个元素在列表中的索引
list1 = ['南京', '天津', '北京', '上海']

index = list1.index('天津')
print(index)

对列表进行排序
list1 = [1, 3, 2, 4, 56, 44, 33, 288]
list1.sort(reverse=True)
print(list1)




'''



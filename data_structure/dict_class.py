
'''
创建一个字典
dict1 = {"key1": "value1", "key2": "value2"}
print(dict1)

创建一个空字典
dict2 = {}
print(dict2)

通过键来访问一个字典里面的key值
dict1 = {"key1": "value1", "key2": "value2"}
print(dict1["key1"])

通过字典的get方法来获取一个值，没有该键，可以指定一个值返回，在这里我们指定的是None
dict1 = {"key1": "value1", "key2": "value2"}
print(dict1.get("key1", None))

遍历字典
dict1 = {"key1": "value1", "key2": "value2"}
for item in dict1:
    print(item, dict1[item])

往字典里面添加一个元素
dict1 = {"key1": "value1", "key2": "value2"}
dict1["key3"] = "value3"
for item in dict1:
    print(item, dict1[item])

判断一个键是否在字典里面
dict1 = {"key1": "value1", "key2": "value2"}
key = "key1"
if key in dict1:
    print(dict1[key])


'''

dict1 = {"key1": "value1", "key2": "value2"}
key = "key1"
if key in dict1:
    print(dict1[key])



# 该函数只有占位符
def test_pass():
    pass


#参数传递
def test_content(name):
    print('我的名字是', name)

#测试有返回值的
def test_return_value(age):
    age = age + 10
    return age

#测试有多个返回值的,返回的是一个元组
def test_multi_value(name,age):
    return name,age

#定一个函数，并且给参数指定默认值

def test_default_value(name=None):
    if name==None:
        print('')



if __name__ == "__main__":
    test_pass()
    #test_content('小明')
    #print(test_return_value(15))
    tuple1=test_multi_value('小明',15)
    print(tuple1)


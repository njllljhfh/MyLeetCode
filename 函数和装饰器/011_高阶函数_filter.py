# -*- coding:utf-8 -*-
print("1 filter()---------------------------------------------")
"""
filter() 方法与 map() 类似，
和 map()不同的是，filter() 把传入的函数依次作用于每个元素，
然后根据返回值的真假决定保留还是过滤掉该元素。
"""


# filter() 的行为等价于：
def homo_filter(func, seq):
    result = []
    for x in seq:
        if func(x):
            result.append(x)
    return result


print("2 下面的示例用于过滤空字符串：---------------------------------------------")
strs = ['hello', ' ', 'world']
ret = filter(lambda x: not x.isspace(), strs)
print(type(ret))
print(ret == iter(ret))
print(list(ret))

print("3 filter() 还可以用于求交集：---------------------------------------------")
# filter() 返回值是一个 filter 对象，它也是一个迭代器。filter() 还可以用于求交集：
a = [4, 0, 3, 5, 7]
b = [1, 5, 6, 7, 8]
print(list(filter(lambda x: x in a, b)))  # 匿名函数   lambda x: x in a

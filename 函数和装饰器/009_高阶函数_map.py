# -*- coding:utf-8 -*-
print("1 ---------------------------------------------")
mapobj = map(str, [1, 2, 3])
print(type(mapobj))

print(mapobj is iter(mapobj))
print(id(mapobj))
print(id(iter(mapobj)))

print(list(mapobj))

print("2 ---------------------------------------------")


def uint_creater():
    i = 0
    while (True):
        yield i
        i += 1


# Python2.x 返回列表，Python3.x 则返回 map 对象，它是一个迭代器。这个改进具有重大的意义，可以用来处理无限序列。
cube = map(lambda x: x * x * x, uint_creater())
for i in cube:
    if i < 10000000000:
        continue
    if i > 10099999999:
        break
    print(i)

print("3 ---------------------------------------------")
funcs = [lambda x: x * x, lambda x: x * x * x]
map_func = lambda f: f(i)  # 看不懂这么写
for i in range(4):
    print(list(map(map_func, funcs)))

print("4 ---------------------------------------------")
# 如果函数列表中的函数具有多个参数如何处理呢？ 只要改写传入函数的参数个数即可，这里计算列表中每个成对的元素的差与和：
funcs = [lambda x, y: abs(x - y), lambda x, y: y + x]  # 函数列表
map_func = lambda f: f(i[0], i[1])  # 传入函数
for i in [[1, 2], [3, 4]]:
    value = map(map_func, funcs)
    print(list(value))

print("4 ---------------------------------------------")
# 如果传入的函数有多个参数，如何处理呢？根据函数参数个数，来传递多个参数序列。例如依次求 pow(2, 2)，pow(3, 3) 和 pow(4, 4) 的值：
print(list(map(pow, [2, 3, 4], [2, 3, 4])))

print("5 ---------------------------------------------")


# map() 函数的本质等同于如下函数：
def homo_map(func, seq):
    result = []
    for x in seq:
        result.append(func(x))
    return result

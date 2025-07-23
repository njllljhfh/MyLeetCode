# -*- coding:utf-8 -*-
print("1 sorted()---------------------------------------------")
"""
sorted() 相对于列表自带的排序函数 L.sort() 具有以下特点：
    1. 将功能扩展到所有的可迭代对象。
    2. L.sort 直接作用在列表上，无返回，sortd() 则返回新的排序列表。
    3. sortd() 是稳定排序，且经过优化，排序速度更快。
"""

print(sorted([5, 2, 3, 1, 4]))
print(sorted((5, 2, 3, 1, 4)))
print(sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}))  # 字典默认使用键名排序

# sorted() 返回列表类型，用它对字符串排序，注意类型转换
print(''.join(sorted("hello")))

print("2 ---------------------------------------------")
# 为 key 指定函数参数，该函数只能接受一个参数，它的返回值作为比较的关键字，比如忽略大小写排序：
sorted_list = sorted("This is a test string from Andrew".split(), key=str.lower)
print(sorted_list)

print("3 ---------------------------------------------")
# 对于复杂对象，我们可以把元素中的部分成员作为排序关键字：
scores = {'John': 15, 'Bill': 18, 'Kent': 12}
new_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)  # reverse 参数默认以升序排序，如果为 True 则以降序排序。
print(new_scores)

print("4 ---------------------------------------------")


# 如果要对自定义的类对象排序，可以选择某个对象成员，下面的示例使用年龄对学生进行排序：
class Student(object):
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

print(sorted(student_objects, key=lambda student: student.age))

print("5 ---------------------------------------------")
# key 参数还可以指定 operator 模块提供的 itemgetter 和 attrgetter 方法。
student_tuples = [('john', 'A', 15),
                  ('jane', 'B', 12),
                  ('dave', 'B', 10), ]
print(sorted(student_tuples, key=lambda student: student[2]))  # age 排序

from operator import itemgetter, attrgetter

print(sorted(student_tuples, key=itemgetter(2)))  # age 排序
print(sorted(student_objects, key=attrgetter('age')))

print(sorted(student_tuples, key=itemgetter(1, 2)))  # 先以 grade 排序，再以 age 排序
print(sorted(student_objects, key=attrgetter('grade', 'age')))

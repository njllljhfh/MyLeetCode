# -*- coding:utf-8 -*-
def keyword_only_args(name="default", *args, age):
    print("name: %s, age: %d" % (name, age))
    print(args)


"""
由于 age 形参位于可变参数之后，那么它的位置是不明确的，此时只能指定关键字 age，
以键值对的方式传递它，被称为关键字参数。此时 args 元组中不会处理它。
"""
keyword_only_args("John", "Teacher", {"Level": 1}, age=30)

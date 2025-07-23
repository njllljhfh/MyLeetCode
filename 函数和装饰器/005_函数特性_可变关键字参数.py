# -*- coding:utf-8 -*-
def keyword_variable_args(name="default", *args, age, **kwargs):
    print("name: %s, age: %d" % (name, age))
    print(args)
    print(kwargs)


keyword_variable_args("John", "Teacher", {"Level": 1}, id="332211", city="New York", age=30)

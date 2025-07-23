# -*- coding:utf-8 -*-
def variable_args(name="default", *args):
    print("name: %s" % name)
    print(args)


variable_args("John", "Teacher", {"Level": 1})

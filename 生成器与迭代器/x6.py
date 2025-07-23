# -*- coding:utf-8 -*-
class App:
    def __init__(self):
        self.view_functions = {}

    # 装饰器工厂，返回的 deco 是一个 装饰器
    def route(self, rule, methods):
        def deco(view_func):
            view_func.allow_methods = [method.upper() for method in methods]
            self.view_functions[rule] = view_func
            return view_func

        return deco


app = App()


@app.route('/', ["POST"])
def index():
    pass


@app.route('/hello', ["GET"])
def hello():
    pass


for rule, view in app.view_functions.items():
    print(rule, ':', view.__name__, "---", f"method = {view.allow_methods}")

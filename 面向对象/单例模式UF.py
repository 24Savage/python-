# 单例模式下，类能且仅能生成一个实例对象

class Singleton(object):

    def __new__(cls, *args, **kwargs):
        print('new')
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

class MyClass(Singleton):

    def __init__(self):
        print('init')
        pass

a = MyClass()
b = MyClass()
print(a is b)
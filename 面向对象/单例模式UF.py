# 单例模式下，类能且仅能生成一个实例对象

class Singleton(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance

class MyClass():

    def __init__(self):
        print('init')
        pass

a = MyClass()
b = MyClass()
print(id(a), id(b))
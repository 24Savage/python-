# __new__返回一个类的实例，该实例就是__init__参数中的self，随后被__init__初始化

class A:
    def __str__(self):
        return 'A'


class B(object):
    def __new__(cls， *args): # 参数cls就是B类型
        '''返回一个实例'''
        print(cls is B)
        return super().__new__(A)   # 利用type创建一个实例

    def __init__(self, x, y): # self就是__new__返回的实例
        '''返回None'''
        pass

# 定义类时有一个关键字参数metaclass
# metaclass必须可调用
# metaclass接受三个参数，name, base, attr，返回一个可以调用的对象，即具有__call__方法

class Meta(type):
    def __new__(cls, name, base, attr): # 定义__call__魔术方法也能够实现返回可调用对象，优先级__new__ > __call__
        print('running class Meta')
        return super.__new__(name, base, attr)  # 可以通过type(cls, name, base, args)来创建一个类型

class C(metaclass = Meta):
    def __init__(self):
        print('running __init__')

# 此时的C已经完全等于Meta.__new__的返回值

# 结合元类，可以实现在定义类的时候修改类
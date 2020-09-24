# 要明确的一点，type 既可以查看对象的类型，也可以生成一个对象
# type(name:str, base:tuple, attr:dict)
def init(self, x):
    self.x = x
MyClass = type('MyClass', (object,), {'__version__':'0.0.0', '__init__': init})
# 前行代码和下面效果完全相同，但使用 class 关键字创建更方便直观
class MyClass:
    __version__ = '0.0.0'
    def __init__(self, x):
        self.x = x
# 可以通过报错信息发现，用 type 创建类的时候其实调用的是 type.__new__，那么 __new__ 是干吗的？往下看：
# type.__new__ 接受四个 parameter：cls、name、base、attr
# 要求 cls 必须是 type 的一种子类，实际上是用 cls 生成了一个对象
# 定义类的时候，可以传入关键字参数 metaclass，要求 metaclass 是 callable
# 编译生成这个类时，会先向 metaclass 传入 name, bases, attr 参数，要求 metaclass 返回一个对象
class Meta(type):
    def __new__(cls, name, bases, attrs):
        print(name, bases, attrs)
        attrs['info'] = 'modded by Meta'
        print('add info to %s'%name)
        return super().__new__(cls, name, bases, attrs)

class Pos(metaclass = Meta):
    def __init__(self, x, y): 
        self.x, self.y = x, y
    def __repr__(self):
        return "({0},{1})".format(self.x, self.y)
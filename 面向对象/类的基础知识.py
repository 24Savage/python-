from math import pi

class Circle():

    cn_name = '圆' # 类变量
    __slots__ = ('_position', '__radius')

    def __init__(self, pos, r): # __init__为对象的初始化方法
        '''self.后的变量称为实例变量
        单下划线和双下滑线都可以组防止被当作模块导入后修改变量
        '''
        self._position = pos # 单下划线在该模块中仍可修改
        self.__radius = r # 加了双下滑线称为private变量，通过dir方法可以看出，它的名字变成了__Circle_private
        
    @property # 通过property装饰器可以把函数当做属性一样调用，修改
    def radius(self):
        return self.__radius
        
    @radius.setter  # 在使用property装饰了radius函数的前提下，使用setter装饰器实现对匿名变量的修改
    def radius(self, r):
        assert r >= 0
        self.__radius = r
        
    @property
    def perimeter(self):
        return self.__radius * 2 * pi
        
    def __lt__(self, other):    # 这样的方法称为魔术方法，例如__lt__代表小于比较的方法，在调用比较运算符时就会以此函数的返回值进行运算
        assert isinstance(other, Circle)
        return self.__radius < Circle.radius
        
    # @staticmethod 静态方法，参数没有self
    # @classmethod  类方法， 参数包括cls
        
if __name__ == '__main__':
    c = Circle( (1, 2),1)
    c.volume = 1   # 试图绑定__slots__中不存在的变量，报错 
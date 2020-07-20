# 在python中，对象之间的关系可分为两种
#     父类——子类的继承关系 type-subtype
#     类型——实例的实例关系    type-instance

class Creature(object):
    pass

class Bird(Creature):
    pass

# 调用类的__bases__属性查看继承的类
# 调用issubclass判断对象是否属于某个类的子类
# <class object>是所有类型的超类
>>>Bird.__bases__
(<class '__main__.Creature'>,)
>>>issubclass(Bird, object)
True


# 使用type方法查看所有对象的类型
# 所有类型的类型都是<class type>
>>>type(Bird)

# 使用isinstance判断对象是否属于某一类型的实例
# 所有类型都是<class type>的实例
# 也就是说所有类型都是type类型的实例
>>>isinstance(Bird, type)
True
>>>isinstance(Bird, Creature)
False

#<class type>是<class object>的子类
# <class object>是<class type>的实例
>>>issubclass(type, object)
True
>>>isinstance(object, type)
True
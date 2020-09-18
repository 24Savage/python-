def say_hi(func):
    @functools.wraps(func) # 为确保func的__name__属性不会改变
    def wrapper(*args, **kwargs):
        print('i\'m a rapper')
        return func(*args, **kwargs)
    return wrapper

@say_hi
def func(a, b):
    print(type(a), type(b))

>>>func((1),(1,))
    i'm a rapper
    <class 'int'> <class 'tuple'>

1 函数也是对象，因此它可以作为另一个函数的参数；
2 同样，函数也可以作为返回值
3 使用魔术方法@，等价于func = say_hi(func)

如果装饰器需要传入参数，需建立三层嵌套：
def say_hello(text):
    def say_hi(func):
        def wrapper(*args, **kwargs):
            print(text)
            print('i\'m a rapper')
            return func(*args, **kwargs)
        return wrapper
    return say_hi

@say_hello('hi')
def func(a, b):
    print(type(a), type(b))

>>>func((1),(1,))
    hi
    i'm a rapper
    <class 'int'> <class 'tuple'>
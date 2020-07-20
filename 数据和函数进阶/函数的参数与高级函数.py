引用内置模块inspect，可以获取对象的参数信息：
import inspect
from inspect import Parameter

def func(a, b=2, *args, c, **kwargs):
    pass
params = inspect.signature(func)
obj = { 
    name: (params.kind, params.default)
    for name,params in params.parameters.items()
    }

无缺省值时，default的值等于Parameter的empty属性
python中，形参parameter有以下几种类型：
    1 POSITIONAL_OR_KEYWORD a,b
    2 VAR_POSITIONAL *args
    3 KEYWORD_ONLY  c
    4 VAR_KEYWORD   **kwargs
1：位置参数或关键字参数，python中没有定义纯位置参数的语法；
2：位置参数集
3：关键字参数，只出现在位置参数集后
4：关键字参数集

使用dir方法可以查看对象的属性：
    __dir__，作用和dir相同；
    __next__，作用和next相同；
    __iter__，作用和iter相同；
        iter 返回一个实现了__next__的对象，然后对这个对象不断调用next()，这也是for循环的机制
    def func():
        for i in range(5):
            yield i

    class A:
        def __iter__(self):
            return func()
            
    for i in A():
        print(i)
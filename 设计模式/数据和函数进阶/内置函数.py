内置的高级函数，map，filter, functools.reduce
1 map
    map(func, *iterables) --> map object
    map接受一个函数和一个iterable对象，返回一个map对象
    obj = map(lambda x:'foobar', (i for i in range(5)))
    map对象是一个迭代器对象
    from collections import Iterator 
    isinstance(obj, Iterator)   >>>True

        另外，list、tuple、str等是Iterable对象，却不是Iterator对象
2 filter
    filter(function or None, iterable) --> filter object
    filter接受一个函数和iterable对象，返回一个filter对象
    函数的返回值一定是bool值
    obj = filter(lambda x: x.islower(), 'AbCdEfG')
3 reduce
    from functools import reduce
    reduce(function, sequence[, initial]) -> value
    function接受两个参数，以序列初始两个值的结果作为参数，
    与序列的下一值进行计算并以此往复
    obj = reduce(lambda x,y : x+y, [i for i in range(5)])
4 eval
    eval(source=, globals=, locals=)
    该函数的作用根据全局变量和局部变量计算source表达式的值
    obj = eval('[1,2,3]') 可直接将该字符串转化为列表
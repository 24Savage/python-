# global：声明变量来自全局变量
# nonlocal：声明变量来自外层嵌套函数
a = 1
def func():
    global a
    a += 1
    b = 1
    def sub_func():
        nonlocal b
        b += 1
    sub_func()
func()
# 对于属于可变对象的变量，就不用进行声明
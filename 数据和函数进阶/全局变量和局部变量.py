a = 2
def func():
    b = 1
    global a # global 关键字声明函数内的a变量是外部的全局变量
    a = 1
    print(locals()) # 打印局部变量

func()
print(globals())    # 打印全局变量

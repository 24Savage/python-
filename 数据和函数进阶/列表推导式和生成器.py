"列表推导式"
obj = [i for i in range(5)]
"把中括号换成()，就定义了一个生成器：class <generator>"
obj = (i for i in range(5))
'''还有字典推导式'''
obj = {k:v for k,v in enumerate(obj)}
"使用以下两种方法会逐一返回生成器中的值，直到抛出StopIteration错误"
next(obj)
obj.__next__()
"要定义一个生成器，需要使用yield关键字"
def yang(n):
    '''打印前n行杨氏三角'''
    arr = [1]
    for i in range(n):
        yield arr
        mid = [arr[i] + arr[i+1] for i in range(len(arr)-1)]
        arr = [1] + mid + [1]
    return '完成'

if __name__ == '__main__':
    obj = yang(5)
    '''只有手动接受StopIteration错误才可以获取生成器的最终返回值，值就包含在错误的values属性中'''
    while True:
        try:
            print(obj.__next__())
        except StopIteration as e:
            print(e.value)
            break
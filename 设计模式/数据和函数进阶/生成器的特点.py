def add(n, i):
    return n+i

def test():
    for i in range(4):
        yield i

g = test()

for n in [1, 10, 5]:
    g = (add(n, i) for i in g)

print(list(g))

# 生成器的特点是只有调用的时候才会进行内部运算，返回yield后的值
# 在该代码中，g的最终表达式为
# n=1   g = ( 1+i for i in test())
# n=10  g = ( 10+i for i in ( n+i for i in test()))
# n=5   g = ( 5+i for i in ( 10+i for i in ( n+i for i in test())))
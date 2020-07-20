# 当一个函数参数太多，而我们在某些时候想固定某些参数简化代码，就可以用偏函数
# 值得注意的是，当固定的参数不是最后一个时，调用函数时需用关键字形式传入参数
from functools import partial

func = lambda x,y,z: x+y+z

func_temp = partial(func, x=1, y=2)
print(func_temp(z=3))
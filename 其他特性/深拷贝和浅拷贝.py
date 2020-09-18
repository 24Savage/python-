# 对象分为可变对象（list, dict, set）和不可变对象（str, tuple，int）
# 对象的复制方式分为深拷贝和浅拷贝，通过copy模块中的deepcopy和copy实现
# 可变对象的copy方法也能实现浅拷贝

from copy import copy, deepcopy

lst = [[1]]
tp = (1,)

new_lst = copy(lst)
new_tp = copy(tp)
# 对可变对象，浅拷贝只拷贝外壳，所含元素不执行操作
# 对不可变对象，浅拷贝完全复制
# 深拷贝对可变对象元素也进行复制
# 列表切片属于浅拷贝
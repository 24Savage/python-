# 一个模块中，_和__开头的都是匿名变量，不应被直接访问(但能够直接访问？不明原因)
# 存在__init__.py文件的的包，__init__.py在包被导入时会被执行
# __init__.py文件中显式声明__all__后，只能导入__all__中的.py文件

import sys
sys.path.append('.\\')
from testmodule import *


obj = dir()
print(obj)
print(test1.__private())
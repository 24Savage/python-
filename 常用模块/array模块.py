# array 模块定义了一种高效的数组，其元素只能为字符、整数或浮点数
# array.array 对象拥有 append pop index remove insert reverse 等方法
import array
import time

arr = array.array('L') # L 代表 32 位 unsign integer，0 ~ 2**32，其余 type code 可使用 help(array) 查看

def test(arr):
    start = time.time()
    rounds = 2**15
    for num in range(rounds):
        arr.append(num)
    print('{0}类型 append 用时：{1}s'.format(type(arr), time.time()-start))
    start = time.time()
    for num in range(rounds):
        arr.insert(0,num)
    print('{0}类型 insert 用时：{1}s'.format(type(arr), time.time()-start))
if __name__ == "__main__":
    # array.array 的 insert 方法要比 list 的快得多
    test(arr)
    test(list())

# 进程是资源分配的最小单位 线程是cpu调度的最小单位
from multiprocessing import Process, Pool
import time

def func(ID):
    print('init func %s'%ID)
    time.sleep(2)
    print('end func %s'%ID)

if __name__ == "__main__":
    p = Pool()  # 默认进程数是 CPU 核心数
    for i in range(8):
        p.apply_async(func, args=(i,))
    print("等待完成")
    p.close()
    p.join()
    print("全部完成")
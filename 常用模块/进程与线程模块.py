import multiprocessing
import threading
import time
# 线程是cpu调度的最小单位，进程是操作系统分配资源和调度的最小单位
# 进程和线程都是一个时间段的描述，是CPU工作时间段的描述，不过是颗粒大小不同
class SubThread(threading.Thread):
    '''
    用 threading.Thread 创建进程，一种方法是传递 callable 对象，另一种是在子类中覆盖 run 方法
    '''
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        print("sub running")
        time.sleep(2)
        print("sub finish")
# 调用 start 来开始线程活动，使用 join 阻塞主线程，直到子线程完成
# 调用 setDaemon 来设置主线程为守护线程，主线程结束后子线程强制结束
class MainThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        print("main running")
        t = SubThread()
        # t.setDaemon(True)
        t.start()
        # t.join()
        print("main finish")

MainThread().start()
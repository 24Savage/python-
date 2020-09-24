from queue import Queue
from collections import deque
from time import time
# collections 还有很多有用类型，如 defaultdict、counter等
q, dq = Queue(), deque()
# 队列 Queue 入队方法为 put，出队方法为 get
# 双端队列 deque 入队方法为 append，出队方法为 popleft，也可以从队尾出队，方法为 pop

if __name__ == "__main__":
    # 由以下可以看出 deque 要比 Queue 快很多
    s = time()
    for _ in range(2**15):
        q.put(None)
        q.get()
    print(time()-s)
    s = time()
    for _ in range(2**15):
        dq.append(None)
        dq.popleft()
    print(time()-s)
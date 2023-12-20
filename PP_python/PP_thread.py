import threading

def job():
    res = 0
    for i in range(10000000):
        res += i

def work():
    import sched
    import ctypes
    import time
    import os
    # 這邊做C lib的呼叫
    tid = threading.current_thread().ident
    print("ThreadID {} start".format(tid))
    libc = ctypes.cdll.LoadLibrary("libc.so.6") # 標準函式庫
    getcpu = libc.sched_getcpu # 宣告C lib的函式
    core = getcpu()
    print("Process {} on CPU Core {} in threadID {} Complete".format(os.getpid(), core, tid))

if __name__ == "__main__":
    worker = threading.Thread
    alist = list()
    for i in range(10):
        alist += [worker(target = work)]
        alist[-1].start()

    for i in range(10):
        alist[i].join()


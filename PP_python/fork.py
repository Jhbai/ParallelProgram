def job(arg):
    import sched
    import ctypes
    import os
    libc = ctypes.cdll.LoadLibrary("libc.so.6")
    getcpu = libc.sched_getcpu
    print("job {} in process {} on CPU {}".format(arg, os.getpid(), getcpu()))

if __name__ == "__main__":
    import os
    core = os.cpu_count()
    workers = list() # 儲存有哪些process的ID在此
    for i in range(10):
        pid = os.fork()
        if pid == 0: # 判斷是否為子process
            job(i)
            os._exit(0)
    for pid in workers:
        os.waitpid(pid, 0)
    print("All Finish, said by main Process {}".format(os.getpid()))



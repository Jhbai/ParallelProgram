import multiprocessing
def job(arg):
    import sched
    import ctypes
    libc = ctypes.cdll.LoadLibrary("libc.so.6")
    getcpu = libc.sched_getcpu
    return arg, getcpu()

if __name__ == "__main__":
    import os
    core = os.cpu_count()
    with multiprocessing.Pool(core) as pool:
        res = pool.imap(job, [i for i in range(core)])
        pool.close()
        pool.join()
    for num, core in res:
        print("{}-th job on core {}".format(num, core))

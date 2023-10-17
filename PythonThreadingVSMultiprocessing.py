# Threading VS Multiprocessing: Running code in parallel for speed upping code
# difference between process and a thread, disadv and adv of both,
# how and why threads are limited by the GIL, how we can use the
# multithreading mod to do stuff

"""
# Process: Instance of a program
    + takes advantage of multiple cpus and cores
    + seperate memory space --> memory not shared between processes
    + great fpr cpu-bound processing
    + new process is started independently from other processes
    + processes are interruptable / killable
    + on GIL for each process --> avoids GIL limitation
    - Heavyweight
    - starting a process is slower than starting a thread
    - more memory usage
    - IPC (inter-process communication) is more complicated

# Thread: entity in a process, a process can have multiple inside
    + all threads within a process share the same memory
    + lightweight
    + starting a thread is faster than starting a process
    + great for I/O-bound tasks, input output tasks such as
        program talking to a slow device like an HDD, using
        the weiht time to switch to other threads and do their
        processing in the mean time
    - threading is limited by GIL: only one thread at a time
    - No effect for CPU-bound tasks
    - not interruptable / killable
    - careful with race conditions

# The GIL (Global Interpreter Lock)
    - a lock that allows only one thread at a time to execute in python
    - needed in CPython because memory management is not thread-safe
        *CPython is the reference python implementation you get when
        you dl and install from Python.org
        - causes memory leaks, references being kept despite needing
            to be destoryed, etc
    - Avoid:
        - use multiprocessing
        - use a different, free threaded Python implementation
            (Jython, IronPython)
        - use Python as a wrapper for third-party libraries
            (C/C++) --> numpy, scipy
                they're wrappers in python that execute code in C
"""

from multiprocessing import Process
import os
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

processes = []
num_processes = os.cpu_count()  # the number of processes should be the num of cpus on your machine

# create processes
for i in range(num_processes):
    p = Process(target=square_numbers)    # target is a function that will be executed by the process
    processes.append(p)

#start processes
for p in processes:
    p.start()

# join
for p in processes:
    p.join()

print('end main')

# ended deep into multiprocessing but need to rewatch, confusing
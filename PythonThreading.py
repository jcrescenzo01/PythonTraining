# Threading, detailed; recap creating multiple threads
# sharing data between threads, how to use locks to prevent
# raise conditions, Daemons and using queues for threat safe data
# conditions.

"""
from threading import Thread
import time

database_value = 0

def increase():     # get and modify database value
    global database_value           # now we can use database_value here
    local_copy = database_value     # get value from db and store in local copy

    # processing
    local_copy += 1                 # increment local_copy
    time.sleep(0.1)                 # processesing should take some time, so wait with sleep()
    database_value = local_copy     # writes the new value into our database

if __name__ == "__main__":

    print("start value", database_value)    # printing the start value "0"

    thread1 = Thread(target = increase)     # created thread1, activating the increase function
    thread2 = Thread(target = increase)     # created thread2, activating the increase function

    thread1.start()     # start thread1
    thread2.start()     # start thread2

    thread1.join()      # wait for thread to complete
    thread2.join()      # wait for thread to complete

    print('end value', database_value)      # print end value, the database value now is 1
                                            # because we have a "raise" condition, which happens
                                            # when two or more threads try to modify the same
                                            # variable at the same time
    print('end main')
"""
"""
    Why its 1 instead of 2, further: basically, start() starts thread1 first, activating the
    increase(), which copies the db value to a local copy, then increments it, only to go for
    time.sleep(0.1), which switches it to thread2. thread2 runs, copies the db value which is 0,
    increments it, then switches back to thread1. Thread1 copies its local copy to the db, and since
    it is done at that point we then switch back to thread2 we switch back to thread2 which also 
    copies 1 into the db
    this is why the end value is 1, and below is how we prevent this:
"""




# VERSION 2.0: PREVENTING THE ABOVE__________________________________________________________________________________________________
"""
from threading import Thread, Lock                      # we add lock to this
import time

database_value = 0
"""
"""
def increase(lock):                                     # increase now takes a lock as an args
    global database_value
    
    lock.acquire()                                      # acquiring the lock
        # a lock prevents another thread to access this code part at the same time
    local_copy = database_value
    # processing
    local_copy += 1
    time.sleep(0.1)
    database_value = local_copy
    lock.release()                                      # release the lock
"""
"""
# increase() with using context manager (with lock:) for easier writing and more legibility
def increase(lock):
    global database_value
    with lock:                                          # acquire and release lock
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy

if __name__ == "__main__":

    lock = Lock()                                       # created a lock here
    print("start value", database_value)

    thread1 = Thread(target = increase, args=(lock,))   # the argument is a lock,
                                                        # and the comma tells that its a tuple
    thread2 = Thread(target = increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('end value', database_value)
    print('end main')
"""
"""
    so the end value is now 2! How this works: the first thread got to lock.acquire in increase(),
    which locked the state. It modified the value and doesnt switch back to thread2 at sleep(0.1) 
    because the state is locked. It runs and copies the local copy to the db, then releases the lock.
    thread2 then starts at lock.acquire again, the db value is already 1 so it increments it again
    during its execution. 
    The second version of increase() uses the context manager version of lock, so that we dont
    have to acquire/release (similar to open/close for file io). Its also more legible in general
"""

"""
    Using Queues in Python:
    Queues are good for thread-safe and process-safe data exchanges and data processing for 
    multithread / multiprocess enviornments.
"""




# VERSION 3.0 - QUEUE USAGE__________________________________________________________________________________________________
"""
# queue usage tutorial

from threading import Thread, Lock
from queue import Queue                         # added Queue capabilities
import time

if __name__ == "__main__":

    q = Queue()

    q.put(1)
    q.put(2)
    q.put(3)

    # 3 2 1 -->
    # 1 enters first, then 2, then 3, each at the left side

    first = q.get()     # takes the 1 from the Queue, putting it in first, leaving 3 and 2 in the queue
    print(first)

    isEmpty = q.empty()             # returns true if the queue is empty
    print(isEmpty)                  # prints False since it isnt

    q.task_done()                   # tells the program that we are done processing with Queue q
    q.join()                        # blocks untill all items in the queue have been gotten and
                                # processed

    print('end main')
"""

from threading import Thread, Lock, current_thread
from queue import Queue                         # added Queue capabilities
import time

def worker(q, lock):
    while True:                 # infinite while loop starts
        value = q.get()         # no values in queue, so it blocks and waits untill they are available
        # processing
        with lock:
            print(f'in {current_thread().name} got {value}')
        q.task_done()           # tells the q that the task is done

if __name__ == "__main__":

    q = Queue()
    lock = Lock()
    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon=True      # background thread that will die when the main thread dies
        thread.start()

    for i in range(1,21):
        q.put(i)                # thread safe, other threads cant write during each exec of this
                            # we reach this statement and exit the main thread loop, stopping the inf loop
    q.join()                    # unblock, continue, then print end main
    print("end main")











"""
# currently havent remade this so ignore this one for now
database_value = 0

def increase(lock):
    global database_value
    with lock:
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy


if __name__ == "__main__":
    lock = Lock()
    print("start value", database_value)

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('end value', database_value)
    print('end main')
"""
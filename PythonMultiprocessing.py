# sharing data, single value process
"""
from multiprocessing import Process, Value, Lock
import time

def add_100(number, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            number.value += 1

if __name__ == "__main__":

    lock = Lock()
    shared_number = Value('i', 0) # single shared value; Value(dataType as a string, starting value)
    print('Number at beginning is', shared_number.value)

    p1 = Process(target=add_100, args=(shared_number, lock))
    p2 = Process(target=add_100, args=(shared_number, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('number at end is', shared_number.value)
"""

"""
# sharing data, array process
from multiprocessing import Process, Value, Array, Lock  # added Array
import time

def add_100(numbers, lock):     # numbers with an s
    for i in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1

if __name__ == "__main__":

    lock = Lock()
    shared_array = Array('d', [0.0, 100.0, 200.0])      # array
    print('Array at beginning is', shared_array[:])     # colon for slicing

    p1 = Process(target=add_100, args=(shared_array, lock))
    p2 = Process(target=add_100, args=(shared_array, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Array at end is', shared_array[:])
"""

"""
# sharing data, array process
from multiprocessing import Process, Value, Array, Lock  # added Array
from multiprocessing import Queue
import time

def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)

def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1*i)

if __name__ == "__main__":

    numbers = range(1, 6)
    q = Queue()

    p1 = Process(target=square, args=(numbers,q))
    p2 = Process(target=make_negative, args=(numbers, q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not q.empty():
        print(q.get())
"""

# Process Pool
# important methods: map, apply, join, close
"""
    Process Pools are for managing multiple processes.
"""

from multiprocessing import Pool
def cube(number):
    return number*number*number

if __name__ == "__main__":
    numbers = range(10)
    pool = Pool()

    result = pool.map(cube, numbers)        # automatically allocates max processes for you,
                                            # typically as many as possible, then splits
                                            # numbers, the iterable, into chunks, executing
                                            #  the function via different processes

    #pool.apply(cube, numbers[0])      # if we just want 1 funct executed by a pool

    pool.close()
    pool.join()

    print(result)


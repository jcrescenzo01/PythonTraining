from threading import Thread
#from multiprocessing import Process
import os
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

if __name__ == "__main__":
    threads = []
    num_threads = 10

    # create processes
    for i in range(num_threads):
        t = Thread(target=square_numbers)
        threads.append(t)

    #start processes
    for t in threads:
        t.start()

    # join, waiting for all processes to finish
    for t in threads:
        t.join()

    print('end main')

# ended deep into multiprocessing but need to rewatch, confusing
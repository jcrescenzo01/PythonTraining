# context managers, what they do, examples, how we can implement our own

"""
# with is a context manager used to open and close files easily
with open('notes.txt', 'w') as file:
    file.write('some todoo...')

# with context manager in similar code form:
file = open('notes.txt', 'w')
try:
    file.write('some todoo...')
finally:    # executed regardless,
    file.close()
"""

from threading import Lock
lock = Lock()
lock.acquire()
#....
lock.release()  # never forget to say the release part!

#with lock:  # context manager

# for our own classes with context managers using enter and exit
class ManagedFile:
    def __init__(self, filename):
        print('init')
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file
    def __exit__(self, exc_type, exc_value, exv_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('exception has been handled')
        #print('exc:', exc_type, exc_value) # exception, then the exception type and value
        print('exit')
        return True


with ManagedFile('notes.txt') as file:
    print('do some stuff...')
    file.write('some todoo...')
    file.somemethod()   # causes an exception
print('continuing') # to see if we reach this code



# doing it with a function
from contextlib import contextmanager
@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f     # tries to yield our resource, temporarily suspending
                    # its own eexecution so we can do some operations with the file
    finally:
        f.close()

with open_managed_file('notes.txxt') as f:
    f.write('some todoo...')
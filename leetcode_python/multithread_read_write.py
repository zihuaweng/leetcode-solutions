import threading
import time

"""
The main difference is that a Lock can only be acquired once. 
It cannot be acquired again, until it is released. (After it's been released, 
it can be re-acaquired by any thread).

An RLock on the other hand, can be acquired multiple times, by the same thread. 
It needs to be released the same number of times in order to be "unlocked".

Another difference is that an acquired Lock can be released by any thread, 
while an acquired RLock can only be released by the thread which acquired it.

"""
# RLock() is a re-entrant lock and allows a thread to call acquire on a lock more than once if it already holds the lock. 
# The reason for using RLock is to avoid a dead lock due to e.g. recursion.
lock = threading.RLock()

def read_write():
    if lock.acquire():   # The return value is True if the lock is acquired successfully, False if not (for example if the timeout expired).
        read_func()
        write_func()
        lock.release()

threads = []
for i in range(5):
    thread = threading.Thread(target=read_write, args=())
    thread.start()
    threads.append(thread)

for thread in threads:
    """Waits for the threads to complete before moving on
       with the main script.
    """
    thread.join()


import threading
import time

my_semaphore = threading.Semaphore(5)


def access(thread_function):
    print(f"{thread_function} is trying to access")
    my_semaphore.acquire()
    print(f"{thread_function} has granted access")
    time.sleep(10)
    print(f"{thread_function} is releasing")
    my_semaphore.release()


for thread_number in range(1, 11, 1):
    my_thread = threading.Thread(target=access, args=(thread_number,))
    my_thread.start()
    time.sleep(1)

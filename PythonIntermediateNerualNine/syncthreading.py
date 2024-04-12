import threading
import time

x = 8192

lock = threading.Lock()


def double_value():
    global x, lock
    lock.acquire()
    while x < 8192 * 2:
        x = x * 2
        print(x)
        time.sleep(1)
    print("Finished the Max")
    lock.release()


def halve_value():
    global x, lock
    lock.acquire()
    while x > 1:
        x = x / 2
        print(x)
        time.sleep(1)
    print("Finished the Min")
    lock.release()


thread_1 = threading.Thread(target=halve_value)
thread_2 = threading.Thread(target=double_value)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
print("Finished All")

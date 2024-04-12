import threading


def printing_one(my_string):
    for i in range(1000):
        print(my_string, end='')


def printing_two(my_string):
    for i in range(1000):
        print(my_string)


thread_1 = threading.Thread(target=printing_one, args=("Hello",))
thread_2 = threading.Thread(target=printing_two, args=(" World!",))

thread_1.start()
# thread_1.join()
thread_2.start()
# thread_2.join()
print("Finished here")

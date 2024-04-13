import queue

my_list = [1, 2, 3, 4, 5, 6, 7]
normal_queue = queue.Queue()
lifo_queue = queue.LifoQueue()
priority_queue = queue.PriorityQueue()

for num in my_list:
    normal_queue.put(num)
    lifo_queue.put(num)

for i in range(len(my_list)):
    print(f"Normal queue element {i + 1}: {normal_queue.get()}", end='')
    print(' -------- ', end='')
    print(f"Lifo queue element {i + 1}: {lifo_queue.get()}")

print("-----------")

"""
    1 -> 100
    priority queue works with priorities and not lifo and fifo
    the lowest the number the higher they priority
"""

priority_queue.put((1, "Amr"))
priority_queue.put((2, "Amira"))
priority_queue.put((5, "FPS"))
priority_queue.put((11, True))
priority_queue.put((8, "Machine gun"))
priority_queue.put((3, "Hassan"))
priority_queue.put((4, "Shaun and Lea"))

while not priority_queue.empty():
    print(priority_queue.get()[1])


# https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/6_Queue/6_queue_exercise.md
import time
from collections import deque
import threading


class Queue:
    def __init__(self):
        self.buffer = deque()

    # def peek(self):
    #     return self.buffer[0]

    def enqueue(self, order):
        self.buffer.append(order)

    def dequeue(self):
        self.buffer.popleft()

    def is_empty(self):
        if len(self.buffer) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.buffer)


foodOrder = Queue()


def place_order(order_list):
    for order in order_list:
        foodOrder.enqueue(order)
        print("Placed Order:", order)
        time.sleep(0.5)


def serve_order():
    time.sleep(0.75)
    while not foodOrder.is_empty():
        order_served = foodOrder.buffer[0]
        print("Served Order:", order_served)
        foodOrder.dequeue()
        time.sleep(2)


orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
t1 = threading.Thread(target=place_order, args=(orders,))
t2 = threading.Thread(target=serve_order)

t1.start()
t2.start()

t1.join()
t2.join()

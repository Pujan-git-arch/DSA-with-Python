# For all exercises use Queue class implemented in main tutorial.

# Design a food ordering system where your python program will run two threads,

# Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
# Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.
# Use this video to get yourself familiar with multithreading in python

# Pass following list as an argument to place order thread,

# orders = ['pizza','samosa','pasta','biryani','burger']
# This problem is a producer,consumer problem where place_order thread is producing orders whereas server_order thread is consuming the food orders. Use Queue class implemented in a video tutorial.

import threading
import time
from learn import Queue # Assuming Queue class is implemented in learn.py # Make sure to implement Queue class in learn.py before running this code.

orders = ['pizza','samosa','pasta','biryani','burger']

def place_order(q):
    for order in orders:
        q.enqueue(order)
        print(f"Placed order: {order}")
        time.sleep(0.5)

def serve_order(q):
    while True:
        order = q.dequeue()
        print(f"Serving order: {order}")
        time.sleep(2)

if __name__ == "__main__":
    q = Queue()
    
    place_thread = threading.Thread(target=place_order, args=(q,)) # Create a thread for placing orders #threading.Thread is used to create a new thread. target specifies the function to be executed in the thread, and args is a tuple of arguments to be passed to the target function.
    
    #tuple is used to pass arguments to the target function. In this case, we are passing the queue instance q as an argument to the place_order function. 
    # # args=(q,) is used to create a tuple with a single element q. The comma is necessary to indicate that it is a tuple, otherwise it would be interpreted as just the value q.
    serve_thread = threading.Thread(target=serve_order, args=(q,))
    
    place_thread.start()
    time.sleep(1)  # Start serve thread 1 second after place order thread is started
    serve_thread.start()
    
    place_thread.join()  # Wait for place order thread to finish
    # serve_thread will run indefinitely, so we won't join it here.
    
    
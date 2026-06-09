from collections import deque

# class Queue:
#     def __init__(self):
#         self.queue = deque()
        
#     def enqueue(self, item):
#         self.queue.append(item)
        
#     def dequeue(self):
#         if not self.is_empty():
#             return self.queue.popleft()
#         raise IndexError("Queue is empty")
    
#     def is_empty(self):
#         return len(self.queue) == 0
    
#     def size(self):
#         return len(self.queue)          

class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, item):
        self.buffer.appendleft(item)  
    def dequeue(self):
        if not self.is_empty():
            return self.buffer.pop()  
        raise IndexError("Queue is empty")
    def is_empty(self):
        return len(self.buffer) == 0
    def size(self):
        return len(self.buffer)
          
    
    
q = Queue()
q.enqueue({'company': 'Google', 'timestamp': '2024-06-01 10:00:00', 'price': 1500})    
q.enqueue({'company': 'Google', 'timestamp': '2024-06-01 11:00:00', 'price': 1500})
q.enqueue({'company': 'Google', 'timestamp': '2024-06-01 12:00:00', 'price': 1500})
print("the front element is",q.buffer[0])  # Output: {'company': 'Google', 'timestamp': '2024-06-01 12:00:00', 'price': 1500}
print("the size of the queue is",q.size(),"and the elements are",q.buffer)  # Output: 3
print("the element to be dequeued is",q.dequeue())   # Output: {'company': 'Google', 'timestamp': '2024-06-01 10:00:00', 'price': 1500}
print("the front element is",q.buffer[0])  # Output: {'company': 'Google', 'timestamp': '2024-06-01 11:00:00', 'price': 1500}
print("the size of the queue is",q.size())  # Output: 2
print(" The elements of the queue are",q.buffer)  # Output: deque([{'company': 'Google', 'timestamp': '2024-06-01 11:00:00', 'price': 1500}, {'company': 'Google', 'timestamp': '2024-06-01 12:00:00', 'price': 1500}])


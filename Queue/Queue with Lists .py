"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Queue:
    def __init__(self, head=None):
        self.storage = [head]
        
    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0]
     
    def dequeue(self):
        return self.storage.pop(0)
    
      
    
# Setup
Queue = Queue(1)
Queue.enqueue(2)
Queue.enqueue(3)

# Test peek
# Should be 1
print(Queue.peek())

# Test dequeue
# Should be 1
print(Queue.dequeue())

# Test enqueue
Queue.enqueue(4)
# Should be 2
print(Queue.dequeue())
# Should be 3
print(Queue.dequeue())
# Should be 4
print(Queue.dequeue())
Queue.enqueue(5)
# Should be 5
print(Queue.peek())

#with simple lists

class SimpleQueue:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.q = []
        self.front = -1
        self.rear = -1

    def enqueue(self, NewValue):
        if self.rear == self.maxSize-1:
            return ('queue is full')
    
        else:
            self.q.append(NewValue)
            self.rear += 1
            return
    
    def dequeue(self):
        if self.front == self.rear:
            return ('queue is empty')

        else:
            self.front += 1 
            self.q.pop(self.front)
            
            

    def show(self):
        print(self.q)



#test

# ll = SimpleQueue(5)

# print('front : ',ll.front) 
# #must be -1


# ll.enqueue(1)
# ll.enqueue(2)
# ll.enqueue(3)
# ll.enqueue(4)

# ll.show()
# #must show 1 2 3 4

# print('front : ',ll.front)
# #must be 0

# print('_______________')

# ll.dequeue()
# print('front : ',ll.front)
# #must be 1

# ll.show()
# # must show 2 3 4





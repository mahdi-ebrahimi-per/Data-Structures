#with simple lists

class CircularQueue:
    def __init__(self, MaxSize):
        self.MaxSize = MaxSize
        self.tail = 0   #rear
        self.head = 0   #front
        self.q    = []
        for i in range(MaxSize):
            self.q.append(None)

    def enQueue(self, NewValue): 
        if self.size() == (self.MaxSize -1):
            return ('queue is full')

        #
        else:
            print('tail : ' ,self.tail)
            self.q[self.tail] = NewValue
            self.tail = (self.tail+1) % self.MaxSize



    def deQueue(self):
        if self.size() == 0:
            return ('queue is empty')
        
        else:
            removedItem = self.q[self.head]
            self.head = (self.head + 1) % self.MaxSize
            return(removedItem)



    def size(self):
        if self.tail >= self.head:
            qsize = self.tail - self.head
        
        elif self.head > self.tail:
            qsize = self.MaxSize - (self.head - self.tail)

        return qsize


    def show(self, show='listy'):
        if show == 'listy':
            return ll.q
        if show == 'for':
            for i in self.q:
                return i



#Test

# ll = CircularQueue(5)

# ll.enQueue(1)
# ll.enQueue(2)
# ll.enQueue(3)
# ll.enQueue(4)


# print(ll.show(show='listy'))

# print(ll.deQueue())

# print('__________________\n' , ll.show(show='listy'))


# ll.enQueue(9)


# print('deleted : ',ll.deQueue())

# print(ll.show(show='listy'))

# ll.enQueue(50)

# print(ll.show(show='listy'))

# ll.deQueue()

# print(ll.show(show='listy'))

# ll.enQueue(60)

# print(ll.show(show='listy'))



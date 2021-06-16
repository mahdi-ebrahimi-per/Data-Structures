class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
            """Get an element from a particular position.
            Assume the first position is "1".
            Return "None" if position is not in the list."""
            current = self.head
            counter = 1
            if position> 1:
                while current and counter < position:
                    if counter == position-1:
                        return current.next
                    else:
                        current = current.next
                        counter+=1
                return None
            elif position==1:
                return self.head


    def insert(self, new_element, position):
        current = self.head
        counter = 1
        if position>1:
            while current and counter <= position-1:
                if counter == position-1:
                    current_copy = current.next
                    new = Element(new_element)
                    new.next = current.next
                    current.next = new
                    break
                else:
                    current = current.next
                    counter += 1
            return None
        elif position==1:
            self.head.value = new_element

    
    def delete(self, value):
        current = self.head
        pre = None
        while current.value != value and current.next:
            pre = current 
            current = current.next
        
        if current.value == value:
            if pre: 
                pre.next = current.next
            else:
                self.head = current.next


    def show_all(self):
        currrent = self.head
        while currrent :
            print(currrent.value)
            currrent = currrent.next



# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)


# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)


# ll.insert(9, 2)
ll.show_all()





class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 

class LinkedList:
    def __init__(self, value):
        new_note = Node(value) 
        self.head = new_note
        self.tail = new_note
        self.length  = 1
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_note = Node (value)
        if self.length == 0:
            self.head = new_note
            self.tail = new_note
        else:
            self.tail.next = new_note    
            self.tail = new_note
        self.length +=1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node (value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = new_node    
            self.head = new_node
        self.length +=1
        return True
    

my_linked_list = LinkedList(1)
my_linked_list.append(2)

print(my_linked_list.pop().value)
print(my_linked_list.pop().value)
print(my_linked_list.pop())

# my_linked_list = LinkedList(11)
# my_linked_list.append(3)
# my_linked_list.append(23)
# my_linked_list.append(7)

# my_linked_list.print_list()

class Node:
    def _init_(self, value):
        self.value = value
        self.next = None
        self.prev = None
 
class DoublyLinkedList:
    def _init_(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
 
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None 
        else: 
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None 
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev 
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
        return True
        return False

def insert(self, index, value): 
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        if (index - 1) == 0:
            temp = self.get(index)
            self.head.next = new_node
            new_node.prev = self.head
            new_node.next = temp 
        else:         
            temp = self.get(index-1)
            temp_next = self.get(index)
            temp.next = new_node
            new_node.prev = temp
            new_node.next = temp_next
            temp_next.prev = new_node
            self.length += 1
        return True
    
def remove(self, index):
    if index < 0 or index >= self.length:
        return None
    if index == 0:
        return self.pop_first()
    if index == self.length - 1:
        return self.pop()
    temp = self.get(index-1)
    temp_next = self.get(index+1)
    temp.next = temp_next
    temp_next.prev = temp
    self.length -=1
    return True

if __name__  == "__main__":
    ll = DoublyLinkedList(11)
    ll.append(3)
    ll.append(23)
    ll.append(7)
    ll.append(2)
    ll.print_list()

#======================================

# my_doubly_linked_list = DoublyLinkedList(7)
# my_doubly_linked_list.append(2)
# my_doubly_linked_list.append(9)

# print('Head:', my_doubly_linked_list.head.value)
# print('Tail:', my_doubly_linked_list.tail.value)
# print('Length:', my_doubly_linked_list.length, '\n')
# print('Doubly Linked List:')

# my_doubly_linked_list.print_list()

#Pop

# my_doubly_linked_list = DoublyLinkedList(7)
# my_doubly_linked_list.append(2)
# my_doubly_linked_list.append(4)

# print(my_doubly_linked_list.pop().value)
# print(my_doubly_linked_list.pop().value)
# print(my_doubly_linked_list.pop().value)
# print(my_doubly_linked_list.pop())

# Prepend

# my_doubly_linked_list = DoublyLinkedList(2)
# my_doubly_linked_list.append(3)

# print('Before prepend():')
# print('----------------')
# print('Head:', my_doubly_linked_list.head.value)
# print('Tail:', my_doubly_linked_list.tail.value)
# print('Length:', my_doubly_linked_list.length, '\n')
# print('Doubly Linked List:')

# my_doubly_linked_list.print_list()
# my_doubly_linked_list.prepend(1)

# print('\n\nAfter prepend():')
# print('---------------')
# print('Head:', my_doubly_linked_list.head.value)
# print('Tail:', my_doubly_linked_list.tail.value)
# print('Length:', my_doubly_linked_list.length, '\n')
# print('Doubly Linked List:')

# my_doubly_linked_list.print_list()

# Pop First

# my_doubly_linked_list = DoublyLinkedList(7)
# my_doubly_linked_list.append(2)
# my_doubly_linked_list.append(4)

# print(my_doubly_linked_list.pop_first().value)
# print(my_doubly_linked_list.pop_first().value)
# print(my_doubly_linked_list.pop_first().value)
# print(my_doubly_linked_list.pop_first())

# Get

# my_doubly_linked_list = DoublyLinkedList(7)
# my_doubly_linked_list.append(2)
# my_doubly_linked_list.append(4)
# my_doubly_linked_list.append(6)

# print('Get node from first half of DLL:')
# print(my_doubly_linked_list.get(1).value)
# print('\nGet node from second half of DLL:')
# print(my_doubly_linked_list.get(3).value)

# Set

# my_doubly_linked_list = DoublyLinkedList(11)
# my_doubly_linked_list.append(3)
# my_doubly_linked_list.append(23)
# my_doubly_linked_list.append(7)

# print('DLL before set_value():')
# my_doubly_linked_list.print_list()
# my_doubly_linked_list.set_value(2,9)
# print('\nDLL after set_value():')
# my_doubly_linked_list.print_list()

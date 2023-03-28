class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def max(self):
        current = self.head
        index = None
        if self.head == None:
            return None
        else:
            while (current != None):
                index = current.next
                while (index != None):
                    if current.value < index.value:
                        temp = current.value
                        current.value = index.value
                        index.value = temp
                    index = index.next
                current = current.next
        return self.head.value

    def append_list(self, list):
        for j in list:
            self.append(j)
        return True


# No.1 
if __name__ == "__main__":
    ll = LinkedList(3)
    ll.append(10)
    ll.append(7)
    ll.append(8)
    print(f"Maximum : {ll.max()}")

# No.2
if __name__ == "__main__":
    ll = LinkedList(3)
    ll.append_list([2,4,8,4,6])
    ll.print_list()

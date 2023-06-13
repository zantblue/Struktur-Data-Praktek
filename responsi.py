def bubble_sort(my_list):
    for a in range (len(my_list) - 1, 0, -1):
        for b in range(a):
            if my_list[b] > my_list[b+1]:
                temp = my_list[b]
                my_list[b] = my_list[b+1]
                my_list[b+1] = temp
    return my_list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        if self.length == 0:
            return False
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next

    def seleksiDewasa(self):
        if self.length == 0:
            return False
        temp = self.head
        while temp != None:
            if temp.value > 300:
                print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def ubahLinkedList(self,list):
        for j in list:
            self.append(j)
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



if __name__ == "__main__":
    Arr = [507,20,241,178,3,257,488,582,357,55,419,480,232,588,362,393,115,133,509,218]
    Arr = bubble_sort(Arr)
    myDLinkedList = DoublyLinkedList(0)
    myDLinkedList.pop()
    myDLinkedList.ubahLinkedList(Arr)  
    myDLinkedList.seleksiDewasa()

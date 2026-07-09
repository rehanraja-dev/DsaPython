
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head   #type:ignore
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data,end='->')
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next #type:ignore
            current.next = prev      #type:ignore
            prev = current
            current = next_node

        self.head = prev 

s1 = LinkedList()

s1.insert_at_beginning(20)
s1.insert_at_beginning(15)
s1.insert_at_beginning(10)
s1.insert_at_beginning(37)
s1.insert_at_beginning(13)
s1.insert_at_beginning(34)
s1.insert_at_beginning(98)

s1.print_list()
s1.reverse()
s1.print_list()

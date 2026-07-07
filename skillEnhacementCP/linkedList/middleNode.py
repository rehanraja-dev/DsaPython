
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

    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next #type:ignore
            fast = fast.next.next

        return slow.data if slow else None
    
     

s1 = LinkedList()

s1.insert_at_beginning(20)
s1.insert_at_beginning(15)
s1.insert_at_beginning(10)
s1.insert_at_beginning(37)
s1.insert_at_beginning(13)
s1.insert_at_beginning(34)
s1.insert_at_beginning(98)
s1.insert_at_beginning(98)

print(s1.find_middle())

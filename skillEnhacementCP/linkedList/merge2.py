class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head   #type:ignore
        self.head = new_node
        
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end='->')
            current = current.next
        print("None")

def merge_sorted_inplace(list1, list2):
    if not list1.head:
        return list2
    if not list2.head:
        return list1

    first = list1.head
    second = list2.head

    if first.data <= second.data:
        merged_head = first
        first = first.next
    else:
        merged_head = second
        second = second.next
        
    current = merged_head
    
    while first and second:
        if first.data <= second.data:
            current.next = first
            first = first.next
        else:
            current.next = second
            second = second.next
        current = current.next
        
    current.next = first if first else second
    
    list1.head = merged_head
    list2.head = None
    return list1

s1 = LinkedList()
s2 = LinkedList()

s1.insert_at_beginning(20)
s1.insert_at_beginning(15)
s1.insert_at_beginning(10)

s2.insert_at_beginning(42)
s2.insert_at_beginning(38)
s2.insert_at_beginning(28)
s2.insert_at_beginning(18)
s2.insert_at_beginning(5)

s = merge_sorted_inplace(s1, s2)

s.print_list()

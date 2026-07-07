
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

    def merge(self,s1,s2):
        p = s1.head
        q = s2.head
        while p and q:
            if p.data < q.data:
                self.insert_at_beginning(p.data)
                p = p.next
            else:
                self.insert_at_beginning(q.data)
                q = q.next
        while p:
            self.insert_at_beginning(p.data)
            p = p.next
        while q:
            self.insert_at_beginning(q.data)
            q = q.next


s1 = LinkedList()
s2 = LinkedList()
s = LinkedList()

s1.insert_at_beginning(20)
s1.insert_at_beginning(15)
s1.insert_at_beginning(10)


s2.insert_at_beginning(42)
s2.insert_at_beginning(38)
s2.insert_at_beginning(28)
s2.insert_at_beginning(18)
s2.insert_at_beginning(5)

s.merge(s1,s2)

print(s1.print_list())
print(s2.print_list())
print(s.print_list())
Tree = [None]*10

def root(key):
    if not Tree:
        print("tree already had root")
    
    else:
        Tree[0] = key

def set_left(key, parent):
    if Tree[parent]:
        Tree[(parent*2)+1] = key
    else:
        print("parent is empty")

def set_right(key, parent):
    if Tree[parent]:
        Tree[(parent*2)+2] = key
    else:
        print("parent is empty")

def print_tree():
    for i in Tree:
        if i is not None:
            print(i,end="-")

root(1)
set_left(2,0)
set_right(3,0)
set_left(4,1)
set_right(5,1)
print_tree()
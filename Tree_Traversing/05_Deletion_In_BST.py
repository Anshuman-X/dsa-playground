class Node:
    def __init__(self,value):
        self.right = None
        self.left = None
        self.data = value

def insert(root,value):
    if(root == None):
        return Node(value)
    if(root.data == value):
        return root
    if(root.data > value):
        root.left = insert(root.left,value)
    else:
        root.right = insert(root.right,value)
    return root

def search(root,value):
    if(root == None):
        print("Element Not Found")
        return 
    if(root.data == value):
        print("Element Found")
        return
    if(root.data > value):
        search(root.left,value)
    else:
        search(root.right,value)
        
def InOrder(root):
    if(root != None):
        InOrder(root.left)
        print(root.data,end = " ")
        InOrder(root.right)
        
def get_successor(root):
    root = root.right
    while(root != None and root.left != None):
        root = root.left
    return root
def get_predessor(root):
    root = root.left
    while(root != None and root.right != None):
        root = root.right
    return root

def delete(root,value):
    if(root == None):
        return root
    if(root.data > value):
        root.left = delete(root.left,value)
    elif(root.data < value):
        root.right = delete(root.right,value)
    else:
        if(root.right == None):
            return root.left
        if(root.left == None):
            return root.right
        else:
            succ = get_successor(root)
            root.data = succ.data
            root.right = delete(root.right,succ.data)
    return root

root = None

root = insert(root,10)
root = insert(root,6)
root = insert(root,9)
root = insert(root,8)
root = insert(root,30)
root = insert(root,25)
root = insert(root,20)
root = insert(root,40)
root = insert(root,35)
root = insert(root,32)
root = insert(root,50)

InOrder(root)
print("\n")
search(root,30)
search(root,45)
print("\n")
root = delete(root,6)
root = delete(root,40)
root = delete(root,8)
InOrder(root)
        
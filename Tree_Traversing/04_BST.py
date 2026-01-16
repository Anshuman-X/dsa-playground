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
        print(root.data,end=" ")
        InOrder(root.right)
        
root=None

root=insert(root,10)
root=insert(root,5)
root=insert(root,8)
root=insert(root,3)
root=insert(root,25)
root=insert(root,9)
root=insert(root,7)
root=insert(root,20)
root=insert(root,15)
root=insert(root,22)

search(root,22)
search(root,40)
InOrder(root)
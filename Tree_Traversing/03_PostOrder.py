class Node:
    def __init__(self,value):
        self.right = None
        self.left = None
        self.data = value

def PostOrder(root):
    if(root != None):
        PostOrder(root.left)
        PostOrder(root.right)
        print(root.data,end=" ")
        
root=Node(1)
root.left=Node(3)
root.left.left=Node(2)
root.left.right=Node(4)
root.right=Node(5)
root.right.right=Node(8)
PostOrder(root)
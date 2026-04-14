class Node:
    def __init__(self,val):
        self.right=None
        self.left=None
        self.data=val
def PreOrder(root):
    if (root!=None):
        print(root.data,end=" ")
        PreOrder(root.left)
        PreOrder(root.right)            
def InOrder(root):
    if (root!=None):
        InOrder(root.left)
        print(root.data,end=" ")
        InOrder(root.right)            
def PostOrder(root):
    if (root!=None):
        PostOrder(root.left)
        PostOrder(root.right)            
        print(root.data,end=" ")
root=Node(3)        
root.left=Node(4)
root.right=Node(5)
root.left.left=Node(1)
root.left.right=Node(2) 
PreOrder(root)
InOrder(root)
PostOrder(root)
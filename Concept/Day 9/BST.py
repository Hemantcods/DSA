class Node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.data=value
def insert(root,value):
    if (root==None):
        return Node(value)
    if (root.data==value):
        return root
    if (root.data>value):
        root.left=insert(root.left,value)
    else:
        root.right=insert(root.right,value)    
    return root
def search(root,value):
    if (root==None):
        print("Element not found ")
        return
    if (root.data==value):
        print("Elemet is found",end='\n')
        return
    if (root.data>value):
        search(root.left,value)
    else:
        search(root.right,value)    

def InOrder(root):
    if (root!=None):
        InOrder(root.left)
        print(root.data,end=" ")
        InOrder(root.right)    

root=insert(None,20)
insert(root,12)
insert(root,18)
insert(root,15)
insert(root,30)
insert(root,40)
InOrder(root)
search(root,21)
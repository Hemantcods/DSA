class Node:
    def __init__(self,info,next=None):
        self.data=info
        self.next=next
        
class SinglyLinkedList:
    def __init__(self,head=None):
        self.head=head
        
    def insert_at_tail(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=Node(data)    
        
    def print_singly_linked_list(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next  
    def insert_at_head(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            temp=Node(data)
            temp.next=self.head
            self.head=temp            
Obj=SinglyLinkedList()
Obj.insert_at_tail(1)
Obj.insert_at_tail(2)
Obj.insert_at_tail(3)
Obj.print_singly_linked_list()
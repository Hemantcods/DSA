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
    def insert_mid(self,value,x): 
        temp=Node(value)
        t1=self.head
        while(t1.next!=None):
            if t1.data==x:
                temp.next=t1.next
                t1.next=temp
                break
            t1=t1.next  
    def delete_LL(self,target):
        t1=self.head
        prev=t1
        if (t1.data==target):
            self.head=t1.next
        while(t1.next!=None):
            if (t1.data==target):
                prev.next=t1.next
                break
            prev=t1
            t1=t1.next
        if(t1.data==target):
                prev.next=None
Obj=SinglyLinkedList()
Obj.insert_at_tail(1)
Obj.insert_at_tail(2)
Obj.insert_at_tail(3)
Obj.insert_mid(4,2)
Obj.delete_LL(1)
Obj.print_singly_linked_list()
class Node:
    def __init__(self,value=None):
        self.prev=None
        self.data=value
        self.next=None
class DoublyLL:
    def __init__(self):
        self.head=None
    def insert_at_end(self,value):
        temp=Node(value)
        if(self.head==None):
            self.head=temp
        else:
            t=self.head
            while(t.next!=None):
                t=t.next
            t.next=temp
            temp.prev=t
    def PrintDLL(self):
        t=self.head
        while(t.next!=None):
            print(t.data,end=" ")
            t=t.next
        print(t.data)
    def insertAtBegning(self,value):
        temp=Node(value)
        if(self.head==None):
            self.head=None
            return
        temp.next=self.head
        self.head.prev=temp
        self.head=temp
    def insertAtMid(self,value,target):
        temp=Node(value) 
        t=self.head
        while(t.next!=None):
            if(t.data==target):
                temp.next=t.next
                temp.prev=t
                t.next=temp
                break
            t=t.next
        if(t.data==target):
            temp.prev=t
            t.next=temp
    def deleteDLL(self,value):
        if self.head==None:
            print("Nothing to delete")
            return
        t=self.head
        if (t.data==value):
            self.head=t.next
            self.prev=None
            return
        while t.next !=None:
            if(t.data==value):
                t.prev.next=t.next
                t.next.prev=t.prev
                return
            t=t.next
        if(t.data==value):
            t.prev.next=None 

                

Obj=DoublyLL()       
Obj.insert_at_end(1) 
Obj.insert_at_end(2)
Obj.insert_at_end(3)
Obj.insertAtMid(5,2)
Obj.deleteDLL(2)

Obj.PrintDLL()
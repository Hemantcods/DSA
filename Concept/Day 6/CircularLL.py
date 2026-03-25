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
            self.head.next=self.head
            self.head.prev=self.head
        else:
            t=self.head
            while(t.next!=self.head):
                t=t.next
            t.next=temp
            temp.next=self.head
            temp.prev=t
            self.head.prev=temp
    def PrintDLL(self):
        t=self.head
        if self.head==None:
            print("the LL is empty")
        while(t.next!=self.head):
            print(t.data,end=" ")
            t=t.next
        print(t.data)
    def insertAtBegning(self,value):
        temp=Node(value)
        if(self.head==None):
            self.head = temp
            temp.next = temp
            temp.prev = temp
            return
        temp.next=self.head
        temp.prev=self.head.prev
        self.head.prev.next=temp
        self.head=temp
        self.head.prev=temp
    def insertAtMid(self,value,target):
        temp=Node(value) 
        t=self.head
        while(t.next!=self.head):
            if(t.data==target):
                temp.next=t.next
                temp.prev=t
                t.next=temp
                break
            t=t.next
        if(t.data==target):
            temp.prev=t
            t.next=temp
            temp.next=self.head
            self.head.prev=temp
    def deleteDLL(self,value):
        if self.head==None:
            print("Nothing to delete")
            return
        t=self.head
        if t.next == self.head and t.data == value:
            self.head = None
            return
        if (t.data==value):
            t.next.prev=self.head.prev
            self.head=t.next
            self.head.prev.next=self.head
            return
        while t.next !=self.head:
            if(t.data==value):
                t.prev.next=t.next
                t.next.prev=t.prev
                return
            t=t.next
        if(t.data==value):
            t.prev.next=t.next
            self.head.prev=t.prev

                

Obj=DoublyLL()       
Obj.insert_at_end(1) 
Obj.insert_at_end(2)
Obj.insert_at_end(3)
Obj.insertAtMid(5,2)
Obj.deleteDLL(2)

Obj.PrintDLL()
# it supports FIFO property
class Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        if len(self.items)==0:
            return True
        else:
            return False
    def insert(self,value):
        self.items.append(value)
    def delete(self):
        if self.isEmpty():
            print('the Queue is empty')
        else:
            return self.items.pop(0)


q=Queue()
q.insert(13)
q.insert(14)
q.insert(15)
print(q.delete())



# double ended Queue (DeQueue)
# both side insertion and deletion


class Dequeue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        if len(self.items)==0:
            return True
        else:
            return False
    def insertAtEnd(self,value):
        self.items.append(value)
    def insertAtFront(self,value):
        self.items.insert(0,value)
    def deleteFromFront(self):
        if self.isEmpty():
            print('the Queue is empty')
        else:
            return self.items.pop(0)
    def deleteFromEnd(self):
        if self.isEmpty():
            print('the Queue is empty')
        else:
            return self.items.pop()
dq=Dequeue()
dq.insertAtEnd(10)
dq.insertAtFront(20)
dq.deleteFromEnd()

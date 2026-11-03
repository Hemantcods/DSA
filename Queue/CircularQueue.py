class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.items=[None]*size
        self.front=-1
        self.rear=-1
    def enqueue(self,value):
        if((self.rear+1)%self.size==self.front):
            print("circular queue is full")
        elif(self.front==-1):
            self.front=self.rear=0
            self.items[self.rear]=value   
        else:
            self.rear=(self.rear+1)%self.size
            self.items[self.rear]=value
    def deque(self):
        if(self.front==-1):
            print('Queue is empty')
        elif(self.front==self.rear):
            self.items[self.front]
            self.front=self.rear=-1
        else:
            print('Queue is empty')
            self.front=(self.front+1)%self.size
cq=CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)



     

        
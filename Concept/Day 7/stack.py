class Stack:
    def __init__(self):
        self.s=[]
    def length(self):
        return len(self.s)  
    def push(self,value):
        self.s.insert(0,value)
    def peek(self):
        if len(self.s)==0:
            raise Exception('Stack is empty')
        else:
            self.s[0]
    def pop(self):
        if len(self.s)==0:
            raise Exception('Stack is empty')
        else:
            return self.s.pop(0)
stk=Stack()
stk.push(10)
print(stk.pop()) 
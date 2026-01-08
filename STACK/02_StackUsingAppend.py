class stack:
    def __init__(self):
        self.s=[]
    
    def length(self):
        return len(self.s)
    
    def push(self,value):
        return self.s.append(value)
    
    def peek(self):
        if len(self.s)==0:
            raise Exception("Stack is empty")
        else:
            return self.s[-1]
        
    def pop(self):
        if len(self.s)==0:
           raise Exception("Stack is empty")
        else:
        
            return self.s.pop(-1)
        
    
stk=stack()
print(stk.length())
stk.push(10)
stk.push(20)
stk.push(30)
print(stk.peek())
print(stk.pop())
print(stk.pop())
print(stk.peek())
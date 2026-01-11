class deque:
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items)==0
    
    def insertAtEnd(self,value):
        return self.items.append(value)
    
    def deleteAtBeg(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            return self.items.pop(0)
        
    def insertAtBeg(self,value):
        return self.items.insert(0,value)
    
    def deleteAtEnd(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            return self.items.pop()
        
dq=deque()
dq.insertAtEnd(10)
dq.insertAtBeg(20)
dq.insertAtEnd(30)
dq.insertAtEnd(40)
dq.insertAtBeg(50)
print(dq.deleteAtEnd())
print(dq.deleteAtEnd())
print(dq.deleteAtBeg())
print(dq.deleteAtBeg())
dq.deleteAtEnd()
dq.deleteAtBeg()

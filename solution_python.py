class EventSourcer():
    # Do not change the signature of any functions
    stack = []
    stack2 = []

    def __init__(self):
        self.value = 0

    def add(self, num: int):
        self.value = self.value + num;
        self.stack.append(1, num);

    def subtract(self, num: int):
        self.value = self.value - num;
        self.stack.append(-1, num);

    def undo(self):
        
        element = self.stack.pop()
        operation = element[0]
        num = element.num
        self.stack2.append( element )
        if operation == 1:
            self.value = self.value - num
            
    
        
        if operation == -1:
            self.value = self.value + num
            

    def redo(self):
       element = self.stack.pop() 
       operation = element[0]
       num = element.num
       self.stack.append( element )
       
       if(operation == 1):
           self.value = self.value + num
           
       if(operation == 1):
           self.value = self.value - num    

    def bulk_undo(self, steps: int):
        while not self.stack.empty:
            self.undo()
            

    def bulk_redo(self, steps: int):
        self.redo()

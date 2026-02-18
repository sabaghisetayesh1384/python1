class stack : 
    def __init__(self , limit = 1000):
        self.st=[]
        self.lim = limit
    def push(self , x):
        if len(self.st) >= self.lim:
           print("stack is full")
           return -1
        self.st.append(x)
    def pop(self):
        if len(self.st) == 0 :
            print("stack is empty")
            return -1
        return self.st.pop()
    def peek(self):
        if len(self.st) == 0 :
            print("stack is empty")
            return -1
        return self.st[-1]
         
test = stack(10)
test.push(57)
test.push(126)
test.push(-10)
k=test.peek()

class stack: Defines the stack.
push(x): Appends x to list if not full.
pop(): Removes last element.
peek(): Returns last element without removing.
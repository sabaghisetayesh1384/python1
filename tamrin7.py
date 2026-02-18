class Queue:
    def __init__(self ,max = 100):
        self.list=[None]* max
        self.front = -1
        self.rear = -1
    def insert(self,x):
        if self.rear >= len(self.list) -1 :
            print("Queue is Full")
            return
        if  self.front == -1 :
            self.front+= 1 
            self.rear+= 1
            self.list[list.rear] = x
            return
        self.rear+= 1 
        self.list[self.rear] = x
    def Del(self):
        if self.front == -1 :
            print("Queue is empty")
            return     
        if  self.front == self.rear :
            k = self.list[self.front]
            self.front = -1
            self.rear = -1
            return k
        k = self.list[self.front]
        self.front+= 1
        return k
    
test = Queue(3)
test.insert(57)
test.insert(32)
test.insert(44)
test.insert(39) #Queue is Full
test.Del()
test.insert(39) #Queue is Full

class Queue: Defines a linear queue.
insert(x): Adds x to the end. BUG: Checks if rear >= len - 1. If rear is at the end, it says 'Full', ignoring free space at start.
Del(): Removes from front.
Test Case: Demonstrates that even after deleting 57, inserting 39 fails because rear is still at the limit.
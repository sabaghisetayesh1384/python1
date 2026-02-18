#"ایندکس(x) های درون پشته را برگرداند."
def find(self,x):
    for i in range(len(self.st)):
        if self.st[i] == x :
           print(i)
#"اولین شامل  (x) را برگرداند"
def find1(self,x):
    for i in range(len(self.st)):
        if self.st[i] == x :
           print(i)
           return
"اخرین ایندکس شامل (x) را چاپ کند"
def find2(self,x):
    for i in range(len(self.st)-1,-1,-1) :
        if self.st[i] == x :
            print(i)
            return
def find2_n(self,x):
    for i in range(len(self.st)):
        if self.st[i] == x :
            p=i
    print(p)                
def find2_n(self,x):
    list=[]
    for i in range(len(self.st)):
        if self.st[i] == x :
            list.append(i)
    print(list[2])
def replace(self,x,y):
    for i in range(len(self.st)):
        if self.st[i] == x :
            self.st[i]=y

find: Print all indices of x.
find1: Print first index of x and return.

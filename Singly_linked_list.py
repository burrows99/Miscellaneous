class Node:
    def __init__(self,data=None):
        self.data=data
        self.nextt=None
        
class LinkedList:
    def __init__(self):
        self.head=Node()
    def Append(self,value):
        newNode=Node(value)
        current=self.head
        while(current.nextt!=None):
            current=current.nextt
        current.nextt=newNode
    def Display(self):
        current=self.head
        l=''
        while(current.nextt!=None):
            current=current.nextt
            l=l+str(current.data)+' -> '
        print(l[:-4])
    def Length(self):
        current=self.head
        l=0
        while(current.nextt!=None):
            current=current.nextt
            l=l+1
        return(l)
    def Delete(self,index):
        try:
            current=self.head
            current_index=0
            while(True):
                previous=current
                current=current.nextt
                if(current_index==index):
                    previous.nextt=current.nextt
                    return
                current_index=current_index+1
        except:
            print('Index out of range!')
    def Insert(self,index,value):
        try:
            newNode=Node(value)
            current=self.head
            current_index=0
            while(True):
                previous=current
                current=current.nextt
                if(current_index==index):
                    previous.nextt=newNode
                    newNode.nextt=current
                    return
                current_index=current_index+1
        except:
            print('Index out of range!')
    def Reverse(self):
        pre=None
        current=self.head
        while(current!=None):
            post=current.nextt #storing in a temporary variable
            current.nextt=pre #changing arrow
            pre=current #traversal
            current=post #traversal
        self.head=pre #setting head node
        print(self.head.data)
    def GetHead(self):
        return(self.head)
    def Set(self):
        l=set()
        current=self.head
        while(current.nextt!=None):
            if(current.nextt.data in l):
                current.nextt=current.nextt.nextt
            else:
                l.add(current.nextt.data)
                current=current.nextt
l=LinkedList()
def f(l,i):
    for x in range(i+2):
        l.Append(i)
for i in range(5):
    f(l,i)
for i in range(5):
    f(l,i)
l.Display()
l.Set()
l.Display()

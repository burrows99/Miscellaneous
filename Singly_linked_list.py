class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self,data='Head'):
        self.head=Node(data)
    def Append(self,element):
        current=self.head
        while(current.next!=None):
            current=current.next
        current.next=Node(element)
    def Display(self):
        current=self.head
        List=[]
        while(current):
            List.append(str(current.data))
            current=current.next
        print(' -> '.join(List))
    def Insert(self,index,element):
        current=self.head
        i=0
        while(i<index):
            current=current.next
            i=i+1
        remaining=current.next
        current.next=Node(element)
        current.next.next=remaining
    def Replace(self,index,element):
        current=self.head
        i=0
        while(i<index):
            current=current.next
            i=i+1
        remaining=current.next.next
        current.next=Node(element)
        current.next.next=remaining
    def Delete(self,index):
        current=self.head
        i=0
        while(i<index):
            current=current.next
            i=i+1
        node_to_be_deleted=current.next
        remaining=node_to_be_deleted.next
        current.next=remaining
    def GetHead(self):
        return(self.head)
    def Reverse(self):
        pre=None
        current=self.head
        while(current!=None):
            post=current.next #storing in a temporary variable
            current.next=pre #changing arrow
            pre=current #traversal
            current=post #traversal
        self.head=pre #setting head node
        current=self.head
        while(current.next.next):
            current=current.next
        current.next=None
        new=Node()
        new.next=self.head
        self.head=new
    def Settify(self):
        current=self.head
        s=set()
        s.add(current.data)
        while(current.next!=None):
            if(current.next.data in s):
                current.next=current.next.next
            else:
                s.add(current.next.data)
                current=current.next
    def IsCycle(self):
        slow_pointer=self.head
        fast_pointer=self.head
        try:
            while(slow_pointer and fast_pointer):
                slow_pointer=slow_pointer.next
                fast_pointer=fast_pointer.next.next
                if(fast_pointer==slow_pointer):
                    return(True)
        except:
            return(False)
    def Cyclify(self,index=0):
        current=self.head
        while(current.next):
            current=current.next
        last=current
        i=0
        current=self.head
        while(i<index):
            current=current.next
            i=i+1
        last.next=current
l=LinkedList()
for i in range(10):
    l.Append(i)
l.Display()
l.Delete(4)
l.Display()

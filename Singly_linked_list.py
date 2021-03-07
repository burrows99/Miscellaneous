class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self,data=None):
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
l=LinkedList(100)
l.Append(100)
l.Append(100)
for i in range(6):
    l.Append(i)
for i in range(6):
    l.Append(i)
l.Display()
l.Reverse()
l.Display()
l.Settify()
l.Display()

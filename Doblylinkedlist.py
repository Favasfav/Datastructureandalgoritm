class Node:
    def __init__(self,data):
         
      self.data=data
      self.next=None
      self.prev=None

class Linkedlist:
   def __init__(self):
      self.head=None
   def addnode(self,data):
        if self.head==None:
           self.head=Node(data)
        else:
           new=Node(data)
           n=self.head
           while  n.next :
                n=n.next
           
           n.next=new
           new.prev=n  
   def print_ll(self):  
      if self.head is None:
          print("np ekjkdfnjkcdfn")
          return
      else:
          n=self.head
          while n:
              print(n.data,"----->")
              n=n.next

li=[1,2,3,4,5]
obj=Linkedlist()
for i in li:
    obj.addnode(i) 

obj.print_ll()    

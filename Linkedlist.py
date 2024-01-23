# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.ref = None


# class Linkedlist:
#     def __init__(self):
#         self.head = None

#     def insertbegning(self, data):
#         new = Node(data)
#         if self.head is None:
#             self.head = new

#         else:
#             new.ref = self.head
#             self.head = new

#     def print__llist(self):
#         if self.head is None:
#             print("no node ")
#             return
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data)
#                 n = n.ref

#     def addend(self, data):
#         if self.head is None:
#             self.head = Node(data)
#         else:
#             n = self.head

#             while n.ref is not None:
#                 n = n.ref

#             new_node = Node(data)

#             n.ref = new_node

#     def add_after(self, data, element):
#         n = self.head
#         new_node = Node(data)

#         while n is not None:
#             print("hhhh",n.data,element)
#             if n.data == element:
#                 break
#             n = n.ref

       
#         new_node.ref = n.ref
#         n.ref = new_node
#     def add_before(self,data,element):
#         n=self.head
#         new=Node(data)
#         while n.ref is not None:
#             if n.ref.data==element:
#                 break
#             n=n.ref
#         if n.ref is None:
#             print("not here")
#             return  
#         new.ref=n.ref   
#         n.ref=new

#     def sortedll(self):
#         n=self.head
#         while n.ref is not None:
#             j=n.ref
#             while j is not None:
#                 if n.data>j.data:
#                     n.data,j.data=j.data,n.data
#                 j=j.ref 
#             n=n.ref       


class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class Linkedlist:
    def __init__(self):
        self.head=None
    def addbeging(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            new=Node(data)
            new.ref=self.head
            self.head=new

    def addbefore(self,data,x):
        n=self.head
        while n.ref is not None:
            if n.ref.data==x :
                break
            n=n.ref   
        if n.ref is None:
            return
        new=Node(data)
        new.ref=n.ref
        n.ref=new        

    def  print__llist(self):
        n=self.head
        while   n is not None:
            print(n.data)

            n=n.ref    

    def sorts(self):
        n=self.head
        while n.ref is not None:
            j=n.ref
            while j is not None:
                if j.data<n.data:
                            j.data,n.data=n.data,j.data
                j=j.ref
            n=n.ref

    def removeduplicate(self):
        n=self.head
        while n.ref is not None:
            j=n.ref
            while j is not None:
                if n.data==j.data:
                    n.ref=j.ref
                j=j.ref
            n=n.ref
    def reverse(self):
        prev=None
        n=self.head
        while n is not None:
            next=n.ref
            n.ref=prev
            prev=n
            n=next
        self.head=prev
obj = Linkedlist()
obj.addbeging(4)
obj.addbeging(34)
obj.addbeging(24)
obj.addbeging(24)
# obj.addend(22)
# obj.addend(2)
# obj.add_after(100, 4)
# obj.add_before(99,100)
# obj.sortedll()
obj.addbefore(12,4)
obj.sorts()
obj.removeduplicate()
obj.reverse()
obj.print__llist()

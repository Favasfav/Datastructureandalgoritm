class BST:
    def __init__(self, key=None) -> None:
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        elif data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:    
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:    
                self.rchild = BST(data)

    def preorder(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def search(self, data):
        if self.key == data:
            print('found')
            return
        if data < self.key:
            if self.lchild:
                print("going left")
                self.lchild.search(data)
            else:
                print('not found')
        else:
            if self.rchild:
                print("going right")
                self.rchild.search(data)
            else:
                print('not found')
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end=' ')       
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder()
    def delete(self,data):
        if self.key==None:
            return self
        if self.key>data:
            if self.lchild:
                self.lchild=self.lchild.delete(data)    
            else:
                print('not found2')      
        elif self.key<data:
            if self.rchild:
                self.rchild=self.rchild.delete(data)
            else:
                print('not found1')
        else:
            if self.lchild is None:
                return self.rchild
            if self.rchild is None:
               return self.lchild
            if self.lchild and self.rchild:
                temp=self.rchild
                while temp.lchild:
                    temp=temp.lchild
                self.key=temp.key
                self.rchild=self.rchild.delete(temp.key)
        return self  
 
def hieght(root):
      if root is None:
          return -1
      left_hiehgt=hieght(root.lchild)
      right_hieght=hieght(root.rchild)
      return max(left_hiehgt,right_hieght)+1

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        n=head
        h=n.next
        if n is None:
            return False
        while n != h:
            if n is  None or h is  None:
                return False
            n=n.next
            h=h.next
        return True    

        
    # def delete(self, data):
    #     if self.key is None:
    #         print('Tree is empty')
    #         return self
        
    #     if data < self.key:
    #         if self.lchild:
    #             self.lchild = self.lchild.delete(data)
    #         else:
    #             print('Element not found')
    #     elif data > self.key:
    #         if self.rchild:
    #             self.rchild = self.rchild.delete(data)
    #         else:
    #             print('Element not found')
    #     else:
    #         if self.lchild is None:
    #             return self.rchild
    #         elif self.rchild is None:
    #             return self.lchild
    #         # Node has both left and right children
    #         successor = self.rchild
    #         while successor.lchild:
    #             successor = successor.lchild
    #         self.key = successor.key
    #         self.rchild = self.rchild.delete(successor.key)
        
    #     return self
          
                                        



root = BST(None)
li = [1, 2, 5, 66, 1, 7, 8, 4, 50]
for i in li:
    root.insert(i)
root.insert(33)    
root.preorder()
print()
root.postorder()
print()
root.inorder()
root.search(2)
root.delete(50)
root.inorder()
a=hieght(root)
print()
print(a)



# class BST:
#     def __init__(self,key=None) -> None:
#         self.key=key
#         self.lchid=None
#         self.rchild=None
#     def insert(self,data):
#         if self.key==None:
#             self.key=data
#         if data>self.key:
#             if self.rchild:
#                 self.rchild.insert(data)
#             else:
#                 self.lchid=BST(data)        

    # def remove(self,data):
    #     if data<self.lchid:
    #         self.lchid.remove(data)
        
    #     if data>self.rchild:
    #         self.rchild.remove(data)   

    #     else:
    #         if self.lchild is None:
    #             return self.rchild
    #         if self.lchid and self.rchild:
    #             temp=self.rchild
    #             while temp.lchild:
    #                 temp=temp.lchid   
    #             self.key=temp.key
    #             self.rchild=self.rchild.remove(temp.key)     
    #     return self

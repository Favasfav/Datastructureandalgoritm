# class Node:
#     def __init__(self) -> None:
#         self.children={}
#         self.end=False

# class Trie:
#     def __init__(self) -> None:
#         self.root=Node()
#     def insert(self, words):
#         n = self.root
#         for w in words:
#             if w not in n.children:
#                 n.children[w] = Node()
#             n = n.children[w]
#         n.end = True  # Set end property on the current node
#     def print_trie(self,node=None,pre=""):
#         if node is None:
#             node=self.root
#         for char,next_node in node.children.items():
#             pre=pre+char
#             if next_node.end==True:
#                 print(pre)
#             self.print_trie(next_node,pre=pre)

#     def prefix_print(self,word):
#         node=self.root
#         prefix=''
#         for char in word:
#             if char not in node.children:
#                 return
#             prefix=prefix+char
#             node=node.children[char]
          
#         self.print_trie(node,prefix)

# t=Trie()
# t.insert('are')
# t.insert('area')
# t.insert('areacode')
# # t.print_trie()   
# t.prefix_print('are')             

            
# class BST:
#     def __init__(self,data) -> None:
#         self.key=data
#         self.lchild=None
#         self.rchild=None
#     def insert(self,data):
#         if self.key==None: 
#             self.key=data
#         if self.key>data:    
#             if self.lchild:
#                 self.lchild.insert(data)
#             else:
#                 self.lchild=BST(data)  
#         if self.key<data:
#             if self.rchild:
#                 self.rchild.insert(data)
#             else:
#                 self.rchild=BST(data)    

#     def inorder(self):
#         if self.lchild:
#             self.lchild.inorder()
#         print(self.key,end=" ")                
#         if self.rchild:
#             self.rchild.inorder()

#     def delete(self,data):
        
#         if self.key>data:
#             if self.lchild:
#                  self.lchild=self.lchild.delete(data)
#             else:
#                 print('not found')     
#         if self.key<data:
#             if self.rchild:
#                     self.rchild=self.rchild.delete(data)     
#             else:
#                 print('not found')
#         else:
#             if self.rchild is None:
#                 return self.lchild
#             if self.lchild is None:
#                 return self.rchild
            
#             if self.rchild and self.lchild:
#                 temp=self.lchild
#                 while temp:
#                     temp=self.lchild
#                 self.key=temp.key
#                 self.rchild=self.rchild.delete(temp.key)    
#         return self        

# bst=BST(10)
# bst.insert(22)
# bst.insert(2)
# bst.insert(4)
# bst.insert(222)
# bst.insert(12)
# # bst.insert(1)
# bst.delete(12)
# bst.inorder()

class Heap:
    def __init__(self) -> None:
        self.heap=[]

    def insert(self,data):
        self.heap.append(data)
        
        self.heapify_min(len(self.heap)-1)    

    def heapify_min(self,index):

        if index<0:
            return None
        parent_index=(len(self.heap)-1)//2
        
        if self.heap[parent_index]>self.heap[index]:    
            self.heap[parent_index],self.heap[index]=self.heap[index],self.heap[parent_index]
            self.heapify_min(parent_index)
    def prints(self):
        print(self.heap)

    # def remove(self,data):
    #     if data not in self.heap:
    #         return
    #     index=self.heap.index(data)
    #     l_index=len(self.heap)-1
    #     self.heap[index],self.heap[l_index]=self.heap[l_index],self.heap[index]
    #     self.heap.pop()
    #     self.heapify(index)
    # def heapify(self,index):
    #     leftindex=2*index+1
    #     rightindex=2*index+2
    #     small=index
    #     if len(self.heap)>leftindex and self.heap[leftindex]<self.heap[index]:
    #         small=leftindex
    #     if  len(self.heap)>rightindex and self.heap[rightindex]<self.heap[index] :
    #         small=rightindex
    #     if small!=index:
    #             self.heap[index],self.heap[small]=self.heap[small],self.heap[index]
    #             self.heapify(small)
    def remove(self,value):
        index=self.heap.index(value)
        self.heap[index],self.heap[len(self.heap)-1]=self.heap[len(self.heap)-1],self.heap[index]
        self.heap.pop()
        self.heapify(index)
    def heapify(self,index):
        lchildindex=2*index+1
        rchildindex=2*index+2
        small=index
        if len(self.heap)<lchildindex and self.heap[index]<self.heap[lchildindex]    :
            small=lchildindex
        if  len(self.heap)>rchildindex and self.heap[rchildindex]<self.heap[index] :
            small=rchildindex    
        if small !=index:
            # swap
            self.heapify(small)    





        
obj=Heap()
obj.insert(40)
obj.insert(4)
obj.insert(440)
obj.insert(44)
obj.insert(22)
obj.insert(5)
obj.remove(440)
obj.prints()




def BFS(node,graph):
    if node not in graph:
        return
    visited=set()
    queue=[]
    queue.append(node)
    while queue:
        current=queue.pop(0)
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                if i not in visited:
                       queue.append(i)

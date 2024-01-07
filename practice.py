# class Node:
#     def __init__(self) -> None:
#         self.children={}
#         self.end=False
# class Trie:
#     def __init__(self) -> None:
#         self.root=Node()
#     def insert(self,word):
#         ptr=self.root
#         for char in word:
#             if char not in ptr.children:
#                 ptr.children[char]=Node()
#             ptr=ptr.children[char]
#         ptr.end=True

#     def print_trie(self, start_node=None, prefix=""):
#         if start_node is None:
#             start_node = self.root

#         for char, child_node in start_node.children.items():
#             new_prefix =  prefix+char
#             if child_node.end:
#                 print(new_prefix)
#             self.print_trie(start_node=child_node, prefix=new_prefix)
#     def prefix(self,word):
#         prefix=""
#         ptr=self.root
#         for char in word:
#             if char not in ptr.children:
#                 print('not in trie')
#                 return
#             prefix=prefix+char
#             ptr=ptr.children[char]
#         self.print_trie(start_node=ptr,prefix=prefix)

# class Node:
#     def __init__(self) -> None:
#         self.children={}
#         self.end=False
# class Trie:
#     def __init__(self) -> None:
#         self.root=Node()
#     def insert(self,word):
#         ptr=self.root
#         for w in word:
#             if w not in ptr.children:
#                 ptr.children[w]=Node()
#             ptr=ptr.children[w]       
#         ptr.end=True
#     def print_trie(self, start_node=None, prefix=""):
#         if start_node is None:
#             start_node = self.root

#         for char, child_node in start_node.children.items():
           
#             new_prefix =  prefix+char
#             if child_node.end:
#                 print(new_prefix)
#             self.print_trie(start_node=child_node, prefix=new_prefix)  

#     def prefix(self,word):
#         pre=""
#         ptr=self.root
#         for chr in word:
#            if chr not in ptr.children:
#                print("not in trie")
#            pre=pre+chr
#            ptr=ptr.children[chr]
#         self.print_trie(start_node=ptr,prefix=pre)          
# obj=Trie()
# obj.insert('hello')  
# obj.insert('he')
# obj.insert("hellodear") 
 
# obj.print_trie()      
# obj.prefix('he')





# graph
graph={}
def addnode(node):
    if node in graph:
        print("node not inside the graph")
        return 
    graph[node]=[]
def addvertices(v1,v2):
    if v1 not in graph:
        return
    if v2 not in graph:
        return
    graph[v1].append(v2)
    graph[v2].append(v1)   

def deletenode(node):
    if node not in graph:
        print("not in graph")
        return
    graph.pop(node)
    for i in graph:
        for j in graph[i]:
            if j==node:
                graph[i].pop(j)
def deleteverices(v1,v2):
    graph[v1].remove(v2)
    graph[v2].remove(v1)


def DFS(node,graph):
    visited=set()
    print(node)
    if node not in graph:
        return
    stack=[]
    stack.append(node)
    print(stack)
    while stack:
        current=stack.pop()
        if current not in visited:
            print(current,end=' ')
            visited.add(current)
            for i in graph[current]:
                stack.append(i)

def BFS(node,graph):
    visited=set()
    queue=[]
    queue.append(node)
    
    while queue:
        current=queue.pop(0)
        if current not in visited:
            print(current,end=" ")
            visited.add(current)
            for i in graph[current]:
                queue.append(i)
def degre(graph):
    c=0
    for i in graph:
        
            c+=len(graph[i])
    return c        

def hieght(graph):
    maximun=0
    for i in graph:
        if len(graph[i])>maximun:
            maximun=len(graph[i])     
    return maximun           

visited=set()
addnode('a')
addnode('b')
addnode('c')
addnode('d')
addnode('e')
addvertices('a','b')
addvertices('a','c')
addvertices('d','b')
addvertices('e','b')
addvertices('e','c')
print(graph)  
# deleteverices('a','c')
 
DFS('a',graph)
print()
BFS('a',graph)
print(degre(graph))                    
print(hieght(graph))
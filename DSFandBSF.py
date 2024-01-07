graph={}

def insert_node(node):
    if node not in graph:
        graph[node]=[]
    else:
        print("nodes is already in graph")    
def add_edges(v1,v2):
    if v1 not in graph:
        print("no node")
    if v2 not in graph:
        print("no node")
    else:
        if v1 in graph:
            graph[v1].append(v2)
            graph[v2].append(v1)



def DFS(node,visited,graph):
    
    if node not in graph:
        print('node not in graph')
        return
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)

def BSF(node,graph):
    if node not in graph:
        print("not in graoh")
        return
    else:
        visited=set()
        queue=[node]
        while queue:
            current=queue.pop(0)
            if current not in visited:
                print(current,end=" ")
                visited.add(current)
                for i in graph[current]:
                    if i not in visited:
                        queue.append(i)

insert_node('a')
insert_node('b')
insert_node('c')
insert_node('d')
insert_node('e')
add_edges('a','b')
add_edges('a','c')
add_edges('c','d')
add_edges('e','b')
print(graph)
print()
visited=set()
(DFS('a',visited,graph))
print()
BSF('a',graph)
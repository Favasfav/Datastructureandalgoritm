graph={}

def add_node(node):
    if node  in graph:
        print('node already in graph',node)
    else:
        graph[node]=[]
def add_edge(v1,v2,cost):
    if v1 not in graph:
        print(v1 ,'not in graph')
    elif v2 not in graph:
        print(v2, 'not in graph') 
    else:
        l1=[v1,cost]
        l2=[v2,cost]
        graph[v1].append(l2)
        graph[v2].append(l1)   

def deletenode(node):
    if node not in graph:
        print("not in graph",node)
    else:
        graph.pop(node)
        for i in graph:
            list1=graph[i]
            for j in list1:
                if node==j[0]:
                    list1.remove(j)      

def remove_edge(v1,v2,cost):
    if v1  not in graph:
        print("not in graph")
    if v2  not in graph:
        print("not in graph")    
    else:
        temp1=[v2,cost]
        temp2=[v1,cost]
        if v1 in graph:
            graph[v1].remove(temp1)   
            graph[v2].remove(temp2)                             
add_node('A')
add_node('B')
add_node('C')
add_edge('A','B',5)
add_edge('A','C',15)
add_edge('A','E',1)
print(graph)  
# deletenode('C')
print()
remove_edge('A','B',5)
print(graph)     



class Heap:
    def __init__(self) -> None:
        self.heap=[]
    def insert(self,value):
        self.heap.append(value)
        self.heapify(len(self.heap)-1)
    def heapify(self,index):
        if index<0:
            return None
        parent_index=(len(self.heap)-1)//2
        
        if self.heap[parent_index]>self.heap[index]:    
            self.heap[parent_index],self.heap[index]=self.heap[index],self.heap[parent_index]
            self.heapify(parent_index)
    def printing(self):
        print(self.heap)     

    def remove(self,value):
        index=self.heap.index(value)
        last_index=len(self.heap)-1   
        self.heap[index],self.heap[last_index]=self.heap[last_index],self.heap[index] 
        self.heap.pop()
        self.heapifyup(index)
    def heapifyup(self,index):
        left_index=2*index+1
        right_index=2*index+2
        small=index
        if left_index<len(self.heap) and self.heap[left_index]<self.heap[index]:
            small=left_index
        if right_index<len(self.heap) and self.heap[right_index]<self.heap[index]:
            small=right_index
        if small!=index:
            self.heap[index],self.heap[small]=self.heap[small],self.heap[index] 
            self.heapifyup(index)




min_heap = Heap()
min_heap.insert(10)
min_heap.insert(4)
min_heap.insert(7)
min_heap.insert(10)
min_heap.insert(12)
min_heap.insert(20)
min_heap.insert(55)
min_heap.insert(100)
min_heap.printing()
print()
min_heap.remove(20)
min_heap.printing()

# class Heap:
#     def __init__(self) -> None:
#         self.heap=[]
#     def insert(self,value):
#         self.heap.append(value)
#         p_index=len(self.heap)-1
#         self.heapify(p_index)
#     def heapify(self,index):
#         parent_index=len(self.heap)//2
#         if self.heap[parent_index]>self.heap[index]  :
#             swap
#             self.heapify(parent_index)      

#     def remove(self,value):
#         index=self.head.index(value)
#         last_index=len(self.head)-1
#         swap
#         pop
#         self.heapiyup(index)
#     def heapifyup(self,index) :
#         left_childindex=2*index+1
#         right_childindex=2*index+2
#         small=index
#         if left_childindex <len(self.heap) and self.heap[left_childindex] >self.heap[index] :
#             small=left_childindex
#         if right_childindex<len(self.heap) and    self.heap[right_childindex] >self.heap[index] :
#             small=right_childindex
#         if small!=index:
#             swap small index
#             self.heapifyup(index)    

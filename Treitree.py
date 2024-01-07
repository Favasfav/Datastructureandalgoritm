
class Node:
    def __init__(self) -> None:
        self.children={}
        self.wordend=False
      
class Trie:
    def __init__(self):
        self.root=Node()
    def insert(self,words):
        node=self.root
        for char in words:
            if char not in node.children:
                node.children[char]=Node()
            node=node.children[char]
        node.wordend=True
    def print_trie(self, node=None, prefix=""):
        if node is None:
            node = self.root

        for char, child_node in node.children.items():
            new_prefix = prefix + char
            if child_node.wordend:
                print(new_prefix)
            self.print_trie(node=child_node, prefix=new_prefix)  
    def search(self,word):
            node=self.root
            for char in word:
                if char not in node.children:
                    return False
                node=node.children[char]
            return node.wordend
                    
    def prefix(self,word):
        node=self.root
        for char in word:
            if char not in node.children:
                return False                
            node=node.children[char]

        return True    
    def prefix_print(self,word):
        ptr=self.root
        pre=""
        for chr in word:
            if chr not in ptr.children:
                print("not in trie")
                return
            pre=pre+chr    
            ptr=ptr.children[chr]
        self.print_trie(node=ptr,prefix=pre)    
obj=Trie()    
words='hello'
obj.insert(words)
obj.insert('hel0000')
obj.print_trie()
print(obj.search('hel00000'))
print(obj.prefix('herr'))
obj.prefix_print("hellll")





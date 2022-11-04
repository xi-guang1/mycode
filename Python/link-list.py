class Node:
    def __init__(self,data = None,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev
        
    def first(self):
        while self.prev != None:
            self = self.prev
        return self
        
    def last(self):
        while self.next != None:
            self = self.next
        return self
            
    def nodes_list(node):
        len_nodes = []
        node = node.first()
        while node != None:
            len_nodes.append(node.data)
            node = node.next
        return len_nodes
        
    def add_next(self,node):
        self.next = node
        node.prev = self
        
    def find(self,a):
        b = 0
        node = self.first()
        while a != b:
            node = node.next
            b += 1
        return node
        
    def append(self,data):
        last = self.last()
        new = Node(data)
        last.add_next(new)
        
'''
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.add_next(node2)
node2.add_next(node3)
#node3.next = node1
#print(node1.next.data)
#print(node2.next.data)
#print(node3.prev.data)
#print(node2.prev.data)
node2.append(4)

print(node2.last().data)
'''

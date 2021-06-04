class Node:
    def __init__(self,data,next_node = None):
        self.data = data
        self.next_node = next_node
    def __repr__(self):
        return "<Node data: %s>" %self.data

class sll:
    def __init__(self):
        self.head = None

    def add(self,data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    def size(self):
        current = self.head
        count = 0 
        while current:
            count += 1
            current = current.next_node
        return count
    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head:%s]"%current.data)
            elif current.next_node is None:
                nodes.append("[Tail:%s]"%current.data)
            else:
                nodes.append("[%s]"%current.data)
            current = current.next_node
        return '->'.join(nodes)

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)
#node = Node(1)
#print(node)

class LinkedList:
    def __init__(self):
        self.head = Node()

    def __repr__(self):
        nodes = []
        current_node = self.head.next
        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next
        return ",".join(nodes)
    
    def append(self,data):
        #as data and next is None at first time , so we can use here just one argument
        node = Node(data)
        if self.head.next is None:
            self.head.next = node
            return
        
        current_node = self.head.next
        while current_node.next:
            current_node = current_node.next
        current_node.next = node
             

    def prepend(self,data):
        node = Node(data,self.head.next)
        print("Node",node,"---","self",self.head.next) #that neans head
        #always stay in font from other node
        self.head.next = node 
        print("after next",self.head.next)

    def insert(self, data, new_data):
        current_node = self.head.next
        while current_node:
            if current_node.data == data:
                new_data = Node(new_data,current_node.next)
                current_node.next = new_data
                break
            current_node = current_node.next

    def search(self,item):
        current_node = self.head.next

        while current_node:
            if current_node.data == item:
                return current_node
            current_node = current_node.next
        return None

    def remove(self,item):
        previous_node = self.head
        current_node = previous_node.next

        while current_node:
            if current_node.data == item:
                break
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            return None
        if self.head == previous_node:
            self.head.next = current_node.next
        else:
            previous_node.next = current_node.next

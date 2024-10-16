class Node:
    """
    An object for storing a single node fo linked list.
    Model two attrubutes - data and the line to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self,data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data
    
class LinkedList:
    """
    Singly linked list
    """
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def size(self):
        """
        Returns the number of nodes in the list
        Takes O(n)
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        
        return count
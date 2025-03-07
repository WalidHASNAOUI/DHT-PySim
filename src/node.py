import random 

class Node: 
    def __init__(self, node_id: int = None):
        # If the node id is given, then assign it, if not generate a random one 
        self.node_id: int = node_id if node_id else random.randint(1, 10000)
        self.left: 'Node' = None
        self.right: 'Node' = None
        
    def join (self, existing_node: 'Node'): 
        """Insert a node in a ring network by finding its right place

        Args:
            existing_node (_type_): _description_
        """
        current = existing_node
        while current.right and current.right != existing_node and current.right.node_id < self.node_id:
            current = current.right
        
        self.right = current.right
        self.left = current
        current.right = self

        if self.right:
            self.right.left = self
            
    def leave(self): 
        """Leave the ring by informing its neightbors
        """
        if self.left: 
            self.left.right = self.right
        if self.right:
            self.right.left = self.left
            
        # reset the current node 
        self.right = None
        self.left = None
        
    def __repr__(self):
        return f"Node({self.node_id})"
import random 
from src.message import Message

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
        
        while True: 
            # Case 1: Insert between two nodes (sorted order)
            if current.node_id < self.node_id < current.right.node_id:
                break

            # Case 2: Edge case - smallest node (wrap-around condition)
            if current.node_id > current.right.node_id and (
                self.node_id > current.node_id or self.node_id < current.right.node_id):
                break

            # Move to the next node
            current = current.right

            # If we have looped around the ring, stop (to avoid infinite loops)
            if current == existing_node:
                break  
            
        self.right = current.right
        self.left = current
        current.right = self
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
        
    def send_message(self, message:Message):
        """Transfert the message to the nearby neighbor

        Args:
            message (Message): message
        """
        print(f"[{self.node_id}] Send message -> {message}")
        
        # Check if the current node is the destination 
        if self.node_id == message.destination.node_id: 
            print(f"[{self.node_id}] Message received ! : '{message.data}'")
        else : 
            # Find the shortest path in the ring
            distance_right = (message.destination.node_id - self.node_id) % 10000
            distance_left = (self.node_id - message.destination.node_id) % 10000
            
            if distance_right < distance_left: 
                print(f"[{self.node_id}] Forwarding to -> {self.right.node_id}")
                self.right.send_message(message)
            else: 
                print(f"[{self.node_id}] Forwarding to -> {self.left.node_id}")
                self.left.send_message(message)
        
    def __repr__(self):
        return f"Node({self.node_id})"
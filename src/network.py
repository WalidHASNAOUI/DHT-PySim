from typing import List
from src.node import Node
from src.message import Message

class Network: 
    def __init__(self):
        self.nodes: List[Node] = []
        
    def add_node(self, node:Node): 
        """Add new node in the ring.

        Args:
            node (Node): new node
        """
        # Check if the ring is empty !!
        if not self.nodes: 
            node.left = node
            node.right = node
        else: 
            node.join(self.nodes[0])
            
        # Add the new node into the ring 
        self.nodes.append(node)
        
        # Sort the ring's nodes 
        self.nodes.sort(
            key=lambda x : x.node_id
        )
        
    def remove_node(self, node: Node): 
        """Drop a node from the ring.

        Args:
            node (Node): a given node
        """
        node.leave()
        self.nodes.remove(node)
        
    def send_message(self, in_source: Node, in_destination: Node, in_data):
        """Send message between two nodes <source, destination>

        Args:
            in_source (Node): source of the message
            in_destination (Node): message destination
            in_data (_type_): the content of the message
        """
        message = Message(in_source, in_destination, in_data)
        in_source.send_message(message)
    
    def display_ring(self): 
        """Display ring's connections
        """
        for node in self.nodes: 
            print(f"{node} -> Right: {node.right}, Left: {node.left}")
        
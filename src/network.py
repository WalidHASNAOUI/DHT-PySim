from typing import List
from node import Node

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
    
    def display_ring(self): 
        """Display ring's connections
        """
        for node in self.nodes: 
            print(f"{node} -> Right: {node.right}, Left: {node.left}")
        
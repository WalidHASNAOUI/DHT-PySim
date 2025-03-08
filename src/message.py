from typing import TYPE_CHECKING

if TYPE_CHECKING: 
    from src.node import Node

class Message: 
    def __init__(self, in_source, in_destination, in_data):
        self.source: Node = in_source
        self.destination: Node = in_destination
        self.data = in_data
    
    def __repr__(self):
        return f"Message({self.source.node_id} -> {self.destination.node_id} : {self.data})"
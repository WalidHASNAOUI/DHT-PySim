import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


from src.node import Node
from src.network import Network

# Create new ring network 
network = Network()

# Add new nodes
n1 = Node(10)
n2 = Node(3)
n3 = Node(5)
n4 = Node(40)

network.add_node(n1)
network.add_node(n2)
network.add_node(n3)
network.add_node(n4)

print(f"The ring network after adding nodes : ")
network.display_ring()

# Drop a node 
network.remove_node(n2)

print(f"\nThe ring network after droping node with id=3 : ")
network.display_ring()




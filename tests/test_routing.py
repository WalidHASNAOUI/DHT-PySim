import sys
import os 
from src.node import Node
from src.network import Network

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


# Create new network
network = Network()

# Add nodes
n1 = Node(10)
n2 = Node(25)
n3 = Node(5)
n4 = Node(40)

network.add_node(n1)
network.add_node(n2)
network.add_node(n3)
network.add_node(n4)

print(f"The ring network after adding nodes : ")
network.display_ring()

# Send a message 
print(f"\nSend a message from [{n1}] to [{n3}]")
network.send_message(n1, n3, f"Hellow, i'm [{n1}]")

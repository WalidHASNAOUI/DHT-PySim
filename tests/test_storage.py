from src.node import Node
from src.network import Network

# Create new network
network = Network()

# Add nodes
n1 = Node()
n2 = Node()
n3 = Node()
n4 = Node()

network.add_node(n1)
network.add_node(n2)
network.add_node(n3)
network.add_node(n4)

print(f"The ring network after adding nodes : ")
network.display_ring()

# Store data 
n2.put("username", "walid")

# Retreive data 
print(n4.get("username"))
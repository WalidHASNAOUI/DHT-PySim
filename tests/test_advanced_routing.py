import sys
import os 
from src.node import Node
from src.message import Message
from src.network import Network

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Create new network
network = Network()

# Add nodes
n1 = Node(2500)
n2 = Node(400)
n3 = Node(1000)
n4 = Node(700)
n5 = Node(100)


network.add_node(n1)
network.add_node(n2)
network.add_node(n3)
network.add_node(n4)
network.add_node(n5)

# Add new long links 
n1.add_long_link(n4)  # Lien long de n1 ➔ n4
n3.add_long_link(n5)  # Lien long de n3 ➔ n5

# Display the ring
print(f"The ring network after adding nodes : ")
network.display_ring()

# Test routing with classical approach 
print("\nClassical Approach : ")
print(f"\nSend a message from [{n1}] to [{n4}]")
network.send_message(n1, n4, f"Hellow, i'm [{n1}]")

# Test routing with long links approach 
print("\nLong links Approach : ")
print(f"\nSend a message from [{n1}] to [{n4}]")
network.send_message(n1, n4, f"Hellow, i'm [{n1}]", 1)
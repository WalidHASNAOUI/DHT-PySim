# Runs a simple DHT Network
from dht.node import Node

if __name__ == "__main__":
    node = Node(1)
    print(f"Node {node.id} created !")
    
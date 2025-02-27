class Node: 
    def __init__(self, node_id):
        self.id = node_id
        self.left_neighboor = None
        self.righ_neighboor = Node
        self.data_store = dict()
        
    def join(self, existing_node): 
        """Join the DHT by finding the correct position in the ring.

        Args:
            existing_node (_type_): _description_
        """
        pass
    
    def leave(self):
        """Leave the DHT, then notify neighboors
        """
        pass
    
    def store_data(self, key, value):
        """Store key-value in the DHT.

        Args:
            key (_type_): _description_
            value (_type_): _description_
        """
        pass
        
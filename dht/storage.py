# Handle storing and retrieving key-value pairs in the DHT

class Storage: 
    def __init__(self):
        self.store = dict()
        
    def put(self, key, value):
        """Store key-value paire.

        Args:
            key (_type_): _description_
            value (_type_): _description_
        """
        self.store[key] = value
        
    def get(self, key):
        """Retrieve a value give a key.

        Args:
            key (_type_): _description_
        """
        return self.store.get(key, None)
        
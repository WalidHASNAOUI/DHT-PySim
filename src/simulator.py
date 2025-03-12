import simpy 
import random
from src.node import Node
from src.network import Network
from src.message import Message

class DHTSimulator: 
    def __init__(self, env):
        self.env = env
        self.network = Network()
        
    def join_node(self): 
        """A new node join the ring within a regular interval.
        """
        while True: 
            yield self.env.timeout(random.randint(1, 5))
           
            # Generate new node
            new_node = Node()
            
            # Add new_node to the ring network
            self.network.add_node(new_node)
            
            print(f"[{self.env.now}] : [{new_node}] has been joined to the ring.")
            
            # Display the ring 
            self.network.display_ring()
            
    def leave_node(self): 
        """A node leave the ring netowork within a regular interval.
        """
        while True:
            yield self.env.timeout(random.randint(3, 10))
            if len(self.network.nodes) > 1: 
                # Chose randomly one node from the ring network 
                node = random.choice(self.network.nodes)
                
                # Ask the ring to remove the choosen node
                self.network.remove_node(node)
                
                print(f"[{self.env.now}] : [{node}] has been left to the ring.")
                
                # Display the ring 
                self.network.display_ring()
                
    def send_message(self): 
        """Random sending of messages between nodes in the ring.
        """
        while True: 
            yield self.env.timeout(random.randint(2, 8))
            if len(self.network.nodes) > 1: 
                # Chose randomly one source node 
                source = random.choice(self.network.nodes)
                destination = random.choice(self.network.nodes)
                
                # To be sure that destination doesn't match source one 
                while destination == source: 
                    destination = random.choice(self.network.nodes)
                    
                # Generate new message
                message = Message(source, destination, f"Message to [{destination}] from [{source}]")
                
                # Sending message using a classical approach or long link one (1/2 chance)
                if random.choice([True, False]):
                    print(f"[{self.env.now}] Sending a msg via a classical approach from [{source}] to [{destination}]")
                    self.network.send_message(source, destination, message)
                else:
                    print(f"[{self.env.now}] Sending a msg via a Long links approach from [{source}] to [{destination}]")
                    self.network.send_message(source, destination, message, 1)
                    
    
    def run(self): 
        """Start the simulation 
        """
        self.env.process(self.join_node())
        self.env.process(self.leave_node())
        self.env.process(self.send_message())
        
        self.env.run(until=50)        
                
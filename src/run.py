import simpy
from src.simulator import DHTSimulator

# Initialiser l'environnement de simulation
env = simpy.Environment()

# Créer une instance de la simulation
simulation = DHTSimulator(env)

# Lancer la simulation
simulation.run()

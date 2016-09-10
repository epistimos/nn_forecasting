from .wrappers import *


datasets = {'AirPassengers': AirPassengers}

def load(name):
   """ loads a given dataset """
    
   return datasets[name]()


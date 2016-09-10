from .wrappers import *


datasets = {'AirPassengers': AirPassengers}


def list():
    """ show available datasets """
    print('Name\t\t\tDescription') 
    print(70*'-')
   
    for k,v in datasets.items():
        print( "%s\t\t%s" % (k,v.__doc__))

def load(name):
   """ loads a given dataset """
    
   return datasets[name]()


# -*- coding: utf-8 -*-
"""
Wrappers for the datasets

@author: Jev Kuznetsov

This module contains a set of wrapper classes that provide an uniform dataset interface.
The classes themselves take care of preprocessing data etc.

"""


import pandas as pd
import numpy as np

# get module path, used for loading data
from os.path import split, join, normpath

path = normpath(join(split(__file__)[0],'data'))


class Dataset():
    """ 
    base class for creating dataset wrappers 

    Parameters from subclass
    --------------------------
    description : a short description about the dataset
    Y : target vector shape Nx1
    X : observation dataset
    
    
    Methods
    -------------
    Xlag(nLags) : returns a [NxnLags] matrix where each column is lagged by n samples

    
    
    """
    
    def __init__(self, description=''):
        
        self.description = description
        
        
    def Xlag(self,nLags=1):
        """ 
        
        generate lagged values 

        Parameters
        ------------
        nLags : int
            number of lags (= number of returned columns)         
    
        """


        lags = range(1,nLags+1)
        data = np.tile(self.Y.values.reshape(-1,1),(1,nLags))
        X = pd.DataFrame(index = self.Y.index, data= data,columns= lags)
        
        
        
        for lag in lags:
            X[lag] = X[lag].shift(lag)
            
        return  X
                
    def __repr__(self):
        
        return self.description + '\nLength=%i rows' % len(self.Y)
    
    


class AirPassengers(Dataset):
    """Dataset containing monthly number of passengers """
    def __init__(self):
        
        Dataset.__init__(self,self.__doc__)
        dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
        self.Y = pd.read_csv(join(path,'AirPassengers.csv'), parse_dates='Month', index_col='Month',date_parser=dateparse)
        
        
    def plot(self):
        
        self.Y.plot()
        
if __name__ == "__main__":
    # quick tests 

    print(path)
    ds = AirPassengers()
    print(ds)
    
    df = ds.Xlag(3)
    df['Y'] = ds.Y    
    
    print(df.head(10))
# -*- coding: utf-8 -*-
"""
Wrappers for the datasets

@author: Jev Kuznetsov

This module contains a set of wrapper classes that provide an uniform dataset interface.
The classes themselves take care of preprocessing data etc.

"""


import pandas as pd


class Dataset():
    """ base class for creating dataset wrappers """
    
    def __init__(self, description=''):
        
        self.description = description
        
    def __repr__(self):
        
        return self.description + '\nLength=%i rows' % len(self.Y)


class AirPassengers(Dataset):
    """Dataset containing monthly number of passengers """
    def __init__(self):
        
        Dataset.__init__(self,self.__doc__)
        dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
        self.Y = pd.read_csv('data/AirPassengers.csv', parse_dates='Month', index_col='Month',date_parser=dateparse)
        
        
if __name__ == "__main__":
    # quick tests 

    ds = AirPassengers()
    print(ds)
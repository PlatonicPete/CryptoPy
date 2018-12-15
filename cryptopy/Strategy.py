# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 11:57:35 2018

@author: user

This class:
    1. Implements a generic skeleton for testing a trading strategy, using a Market object
       for data input. It provides a number of common methods and useful variables
    2. Can output a useful standard "Strategy Report" ***xxx (a pdf file, or maybe a separate type of
       Python object which can then output different file types)
"""

class Strategy:
    
    
    def __init__(self):
        
        #These need to be done up ***
        self.profit=[]#The time series for profit
        self.final_profit=0#final profit
        self.target_market=0#Market object to deal with
        pass
    
    def run_strategy():
        """This runs the strategy and populates/re-populates the result variables"""
        pass
    
    def run_strategies():
        """This runs the strategy a number of times for different parameters as
           specified in an input argument"""
        pass
    
    def create_report():
        """This will in some way or another output a strategy report"""
        pass


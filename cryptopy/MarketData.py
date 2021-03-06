# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 11:54:54 2018

@author: user

This class is produced by the MarketDataGrabber ***xxx class as a uniform form of
storing raw data fetched from different exchange APIs.

This class:
    1. Stores fetched data from an exchange in an exchange-independent standard 
       form

"""

class MarketData:
    
    def __init__(self):
        
        #the request params
        self.interval = 0
        self.pair = ""
        self.exchange = ""
        
        #usual stuff received
        self.time = []
        self.open = []
        self.high = []
        self.low = []
        self.close = []
        self.vwap = []#volume_weighted_average = []
        self.volume = []
        
    def __str__(self):
        output_string = "MarketData object: " + str(self.pair) + " @ " + str(self.exchange) + " - " + str(self.interval) +"min"
        return output_string
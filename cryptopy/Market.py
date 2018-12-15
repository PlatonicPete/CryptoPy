# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 11:53:09 2018

@author: user

This class:
    1. Stores complete data (including accross multiple timeframes) about a particular,
       specific tradeable market, for example: LTC-USD on Kraken.com
    2. Provides some common useful indicators on the data as methods(moving average, etc)

This class can be used as data for the Strategy class, or a strategy function to assess profit
"""

class Market:
    
    def __init__(self):
        
        #The main marketdata object
        self.market_data = []
        
        #main timeframe, for single timeframe work
        self.main_timeframe_interval = 0
        self.time = []
        self.open = []
        self.high = []
        self.low = []
        self.close = []
        self.volume_weighted_average = []
        self.volume = []
        
        #name data - CONSIDER REVISING TO GENERALISE TO CRYPTO-CRYPTO pairs,
        #not just CRYPTO-FIAT
        self.pair = ""
        self.pair_name = ""
        self.crypto_name = ""
        self.fiat_name = ""
        self.pair_type = ""
        
        #some storage structure for multiple timeframes needs to be devised
        
        
        pass
    
    
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 13:55:53 2018

@author: user
"""

import krakenex#***xxx
import numpy as np
import datetime

#INTRA PACKAGE IMPORTS _I STILL DONT UNDERSTAND THESE
from cryptopy.exchanges.Exchange import Exchange
from cryptopy.MarketData import MarketData

class KrakenExchange(Exchange):
    """
    This class:
        1. Makes requests via krakenex module to the Kraken cryptocurrency exchange API
        2. Returns request data as raw dict or MarketData object
    """
    
    def __init__(self):
        
        #initialize the API class from krakenex which will handle the requests
        self._api_handler = krakenex.API()
        self._last_result = None #Stores the latest error less result of a query
        self._last_query = None #Stores the response to the latest query made
        
        self.whitelist = ["DASH","QTUM"]
    
    def get_ohlc(self, pair, interval, since=0):
        """
        This method returns the OHLC data as given by Kraken for a particular pair, interval,
        and since a particular date. Since = 0 gives all past data availiable via the API.
        
        Args:
            pair - human-readable pair code for which to fetch data
            interval - the trading interval for which to fetch data
            since - timestamp since when to fetch data, default fetches all availiable data
        
        Returns:
            Dictionary of arrays in form [timestamp, open, high, low, close, vwap, volume, count],
            with one array per each data point
        """
        ##error handling of function input***XXX
        
        #Uppercase-izes and truncates to 6 chars
        pair = self.pair_digest(pair)
        
        
        
        #AT THIS STAGE THE pair ARGUMENT HAS :
        #    1. Been coverted to all uppercase
        #    2. Sent a warning if it was longer than six chars
        
        #modify pair for kraken pair, e.g. LTCUSD -> XLTCZUSD,
        #includes BTC -> XBT change
        k_pair = self.krakenise_pair(pair)
        
        
        #prepping the input parameters for the API query
        data = { 
                "pair":k_pair, 
                "interval":interval, 
                "since":since
                }
        
        #make API query
        result = self._api_handler.query_public("OHLC",data = data)
        
        #Record the result of the last query regardless or
        self._last_query = result
        
        #if result is not error, make last_result the result
        if(result['error'] == []):
            self._last_result = result['result']
        else:
            #error handling code***XXX
            raise Exception("TO BE CODED IN. THE API HAS RETURNED AN ERROR"+str(result['error']))
        
        #return the result of the query, trimming off the error messages, 
        #which should have been dealt with earlier
        #The data is also stripped of the pair label.
        #so, THE DATA IS NOT LABELLED WITH THE CURRENCY PAIR
        return result['result'][str(k_pair)]
    
    def krakenise_pair(self,pair):
        """
        Modifies pair for Kraken API by inserting X and Z, as well as converting BTC
        into XBT
        
        e.g. LTCUSD -> XLTCZUSD
        e.g. ETHBTC -> XETHZXBT
        """
        #First check if we have 3 or 4 letter crypto symbol
        first = None
        second = None
        
        #use slice objects to then refer to the first or second in the currency pair
        if(len(pair)==6):
            first = slice(0,3)
            second = slice(3,6)
        elif(len(pair)==7):
            first = slice(0,4)
            second = slice(4,7)
        
        #alternative bitcoin symbol
        #Kraken does not recognise BTC, uses XBT instead.
        #If the user uses BTC, automatically convert to XBT
        if(pair[first]=="BTC"):
            pair = "XBT"+pair[second]
        
        if(pair[second]=="BTC"):
            pair = pair[first]+"XBT"
        
        #insert X or Z depending on crypto or fiat***XXXthis could be improved
        if(pair[second]=="XBT" or pair[second]=="ETH"):
            #insert X and X
            if(len(pair)==7):
                #The API does not add the x and z for 4 letter symbols
                return pair
            else:
                return "X"+str(pair)[first]+"X"+str(pair[second])
        else:
            #insert X and Z at correct positions
            if(len(pair)==7):
                #The API does not add the x and z for 4 letter symbols
                return pair
            else:
                return "X"+str(pair)[first]+"Z"+str(pair[second])
    def get_market_data(self,pair,interval,since=0):
        """
        Gets market data and returns a MarketData object
        """
        #fetch the data
        raw_response = self.get_ohlc(pair,interval,since)
        
        #parse data into a market data object
        market_data = MarketData()
        
        market_data.interval = interval
        market_data.pair = pair
        market_data.exchange = "Kraken"
        
        market_data.time = np.array([datetime.datetime.fromtimestamp(int(i[0])) for i in raw_response])
        market_data.open = np.array([float(i[1]) for i in raw_response])
        market_data.high = np.array([float(i[2]) for i in raw_response])
        market_data.low = np.array([float(i[3]) for i in raw_response])
        market_data.close = np.array([float(i[4]) for i in raw_response])
        market_data.vwap = np.array([float(i[5]) for i in raw_response])
        market_data.volume = np.array([float(i[6]) for i in raw_response])
        
        return market_data

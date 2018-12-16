# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 23:34:28 2018

@author: user
"""
import cryptopy.exchanges.kraken
import matplotlib.pyplot as plt

exchange = cryptopy.exchanges.kraken.KrakenExchange()
m_data = exchange.get_market_data("XBTUSD",15)

plt.figure(figsize=(14,9))
title = str(m_data)[18:]
plt.title(title)
plt.plot(m_data.time,m_data.close)
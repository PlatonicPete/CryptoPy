# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 01:52:16 2018

@author: user
"""

import requests
import numpy as np
import hashlib
import urllib.parse
import hmac
import time

private_key = "awgSmM2KRjw7fwuWi9zr2l9C4kuzTlfAZWmiNZ0mmwc40f8LIO5tdLqvDNbCaw0sSfbPfWTr3zVxCk1IbhPjMg=="

head_init = {"API-Key":"rmpWGPkdnhEvhprlm9ANFGaBqGItS8ayR1Tbc0K0Uk5EV54tTPNTpDOS",
             "API-Sign":""
             }

def buy():
    pass

def sell():
    pass

def make_sign(preq, path):
    payload = {"asset":"ZUSD"}
    paybytes = urllib.parse.urlencode(payload).encode('utf-8')
    sign = hmac.new(private_key,paybytes,hashlib.sha512).hexdisgest()
    head_init["API-Sign"]=sign
    req = requests.Request("POST","https://api.kraken.com/0/private/TradeBalance",data=paybytes,headers=head_init)
    
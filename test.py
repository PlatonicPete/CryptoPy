# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 02:13:11 2018

@author: user
"""

import requests

r = requests.post("http://www.wikipedia.org/",data={"hello":"hi"})
print(r.data)

# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 00:26:52 2019

@author: yasha
"""

import pymongo
from pymongo import MongoClient
import pprint

client = MongoClient()
client = MongoClient('localhost:27017') 
db = client['numtest']
TaxiData =db.TaxiData

TaxiData = TaxiData.find()

for TaxiD in TaxiData:
    pprint.pprint(TaxiD)













#pprint.pprint(db)
#db = client.Taxi
#collection = db.TaxiJan

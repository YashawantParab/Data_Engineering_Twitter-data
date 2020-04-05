# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 10:15:28 2019

@author: YP
"""

import pymongo
from pymongo import MongoClient
import pprint
#client = MongoClient()
client = MongoClient('localhost:27017')
db = client['Taxi']
collection_TaxiJan =db['TaxiJan']
founded_TaxiJan = collection_TaxiJan.find()
pprint.pprint(founded_TaxiJan)

#result = TaxiJan.find()
#from mongoengine import *
#connect('Taxi', host='localhost', port=27017)
#MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True, read_preference=Primary())

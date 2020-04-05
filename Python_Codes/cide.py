# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 19:13:28 2019

@author: yasha
"""

from pymongo import MongoClient
import matplotlib.pyplot as plt
import pandas as pd
import csv
import json

"""
plt.plot([1,2,3],[5,7,4])
plt.show()
"""

# df = pd.DataFrame(data=d)
client = MongoClient('localhost:27017')
db = client.Taxi
collection = client.Taxi.TaxiDec
"""
collection = db.settings.find() # I am getting everything !
for x in collection:
    print(x)
    """
# df = pd.DataFrame(collection)

cursor = collection.find({}, {
                                "_id": 0,
                                "total_amount": 1,
                                }).limit(50)

for data in cursor:
    # print(data);
    df = pd.DataFrame.from_records(cursor)
    print(df)

cursor1 = collection.find({}, {
    "_id": 0,
    "total_amount": 1,

}).limit(50)

for data1 in cursor1:
    # print(data);

    df1 = pd.DataFrame.from_records(cursor1)
    print(df1)
    
    """
ylabel = df1
plt.plot(xlabel, ylabel)
plt.show()
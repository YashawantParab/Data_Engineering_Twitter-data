# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 23:32:35 2019

@author: yasha
"""
from pymongo import MongoClient
import matplotlib.pyplot as plt
import pandas as pd
import csv
import json

client = MongoClient('localhost:27017')
db = client.Taxi
collection = client.Taxi.TaxiDec

pipeline = collection.aggregate(
        [
                {"$match" : {"lpep_pickup_datetime": {"$gte": "2018-01-01 00:00:00","$lt": "2018-01-01 23:59:59"}}},
                {"$group" : {"_id" : "$lpep_pickup_datetime" , "fare_amount" : {"$sum" : "$fare_amount"}}}
        ]
)		
cursorTotalTripsCount = collection.aggregate(pipeline)
#print(cursorTotalTripsCount)
#data =  pipeline.aggregate(pipeline=cursorTotalTripsCount)
for cursor in cursorTotalTripsCount:
    arrAggregateHourlyValues[idx1,0] = cursor["TotalTripsCount"]
    cursorTotalTripsCount.close()
#print(Taxi_data)

"""
for cursor in cursorTotalTripsCount:
    arrAggregateHourlyValues[idx1,0] = cursor["TotalTripsCount"]
    cursorTotalTripsCount.close()

df = pd.DataFrame.from_records(fuel_data)
print(df)


brand_count = collection.aggregate([{'$group' : {'_id' : '$brand', 'count' : {'$sum' : 1}}}, {'$match' : {'count' : {'$gt' : 1}}}, {'$sort' : {'count' : -1}}, {'$project' : {'brand' : '$_id', 'count' : 1, '_id' : 0}}])
dflc = pd.DataFrame.from_records(brand_count)
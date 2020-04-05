# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 12:06:13 2019

@author: yasha
"""

client = MongoClient('localhost:27017')

collection = client.NYC4.NYCTaxiJan4



TaxiData = collection.aggregate([
        {'$unwind': '$NYCData.fare_amount'},
       
        {'$group': {'_id': '$NYCData.fare_amount.text', 'FareAmountCount' : {'$sum' : 1}}},

        {'$sort': {'FareAmountCount' : -1}}, {'$limit' : 10},
        
        {'$project' : {'NYCData' : '$_id', 'FareAmountCount' : 1, '_id' : 0 }}
    
        ])


df = pd.DataFrame.from_records(TaxiData)
print(df) 

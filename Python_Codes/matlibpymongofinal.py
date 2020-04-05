# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 12:49:23 2019

@author: yasha
"""

from pymongo import MongoClient
import matplotlib.pyplot as plt
import json
"""
plt.plot([1,2,3],[5,7,4])
plt.show()
"""

client = MongoClient('localhost:27017')
db = client.Taxi
collection = client.Taxi.TaxiJan



cursor = collection.find({},
                       {"_id" :0,
                          "payment_type": {"$gte" : 1, "$lt" : 3}}).sort([("PULocationID", -1)]).limit(5)
                         #{"$gt": "2"}

for data in cursor:
   print(data)
  
"""
for json_dict in cursor:
    if 'payment_type' in json_dict.keys():
        print (json_dict['payment_type']) #get the value data of PULocation
       
"""   
""" 
    cursor_count = cursor.count()
print(cursor_count)
"""
"""
cursor = collection.find( {}, {
        "_id" :0, 
        "PULocationID" : 1} ).sort([("PULocationID", -1)]).limit(5)
"""   
        
  #  for key,value in json_dict.iteritems():
   #     print("key: {0} | value: {1}".format(key, value))
        
        
#new = data["PULocationID"].str.split(" ", n = 1, expand = True)
#print(new)

""" 
x= data
plt.plot(x)

"""
"""
pipeline = [ {"$match": 
    {"RatecodeID": {"$gte": "50", "$lt": "90"}}
    } ,
    {"$group": {"_id": 1, "TotalTripsCount": {"$sum": 1}}}
    ]
cursorTotalTripsCount = collection.aggregate(pipeline)
for cursor in cursorTotalTripsCount:
    db.Taxi.aggregate({$match: { RatecodeID: "A"}},
                      [i  dx1,0] = cursor["TotalTripsCount"])
"""
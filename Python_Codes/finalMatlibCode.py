# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 19:09:23 2019

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

#df = pd.DataFrame(data=d)
client = MongoClient('localhost:27017')
db = client.Taxi
collection = client.Taxi.TaxiDec

#df = pd.DataFrame(collection)

cursor = collection.find({},{
        "_id" :0,
        "total_amount" : 1,
        }).limit(50)

    
for data in cursor:
    print(data);
    
    df = pd.DataFrame.from_records(cursor)
    print(df);
    
    
cursor1 = collection.find({},{
        "_id" :0,
        "total_amount" : 1,
        
        }).limit(50)
    
for data1 in cursor1:
   # print(data);
    df1 = pd.DataFrame.from_records(cursor1)
    print(df1)
     
    
    
    x= df
       y= df1
       plt.plot(x,y)
       plt.show()      

plt.bar()
       
       
       
""""
xlable = df

       
ylabel = df1
plt.plot(xlabel, ylabel)
plt.show()















"""
       plt.xlabel('PULocationID')
       plt.ylabel('PULocationID')
       plt.title('His togram');
"""
       
     
        
       
       
       
"""from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(df, df1, test_size = 0.2, random_state = 0)
 """      
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       """
       
"""
"""for json_dict in cursor:
    if 'PULocationID' in json_dict.keys():
        print (json_dict['PULocationID']) #get the value data of PULocation
       
        #plt.xlabel('PULocationID')
        #plt.title('His togram');
"""
        """
for data in cursor:
    print(data);
    plt.xlabel('PULocationID')
#data = csv.writer("x.csv", 'wt)
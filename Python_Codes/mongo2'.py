# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 19:31:31 2019

@author: yasha
"""

import os
import csv
from json import dumps
from time import sleep
from kafka import KafkaProducer

#Changing default working directory
csv.register_dialect('CodeCode1',delimiter = ',',skipinitialspace=True)

#Creating producer object; Lamba function used to serialize the data and encode it to utf-8 format
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'))

#Reading csv to a dictionary and sending the data with the topic name 'lord-overload'
with open("Y:\SRH Heidelberg\Modules\DataEngg\Taxi Data\Jan\green_Jan.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile, dialect = 'CodeCode1')
    for row in reader:
        #data = {'FuelData' : row}
        producer.send('CodeCode1', value=row)
        
        #print(dict(row))

#Flushing csv file object
csvfile.close()
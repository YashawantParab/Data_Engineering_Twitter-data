# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("Hello Anaconda")


import os
import csv
from json import dumps
from time import sleep
from kafka import KafkaProducer

#Changing default working directory
csv.register_dialect('taxijan',delimiter = ',',skipinitialspace=True)

#Creating producer object; Lamba function used to serialize the data and encode it to utf-8 format
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: dumps(x).encode('utf-8'))

#Reading csv to a dictionary and sending the data with the topic name 'lord-overload'
with open("Y:\SRH Heidelberg\Modules\DataEngg\Taxi Data\Jan\GreenJan100.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile, dialect = 'taxijan')
    for row in reader:
        #data = {'NYCData' : row}
        producer.send('Presentaion07', value=row)
        
        #print(dict(row))

#Flushing csv file object
csvfile.close()
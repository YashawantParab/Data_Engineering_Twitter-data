# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 19:19:51 2019

@author: yasha
"""

from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads
from datetime import datetime

# import requests

consumer = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    #     auto_commit_interval=50,
    group_id='my-group',
    #consumer_timeout_ms=5000
    value_deserializer = lambda x: loads(x.decode('UTF-8'))

consumer.subscribe(['testTopic2'])
client = MongoClient('localhost:27017')
collection = client.testTopic2Data.newYorkTaxi
# db.testTopic1Data.drop()

for message in consumer:
    message = message.value
collection.insert_one(message)
print('{} added to {}'.format(message, collection))

print('ALL DONE ALL DONE ALL DONE')




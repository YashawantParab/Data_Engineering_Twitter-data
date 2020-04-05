from kafka import KafkaConsumer
#from pymongo import MongoClient
from json import loads
from datetime import datetime

consumer = KafkaConsumer(
    'KAFKA_T',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    #     auto_commit_interval=50,
    #     group_id='my-group',
    value_deserializer = lambda x: loads(x.decode('UTF-8')))


#client = MongoClient('localhost:27017')
#collection = client.KAFKA_T.KAFKA_T
# db.testTopic1Data.drop()

for message in consumer:
    message = message.value
    collection.insert_one(message)

    print('{} added to {}'.format(message, collection))

print('ALL DONE ALL DONE ALL DONE')

# from kafka import KafkaConsumer
# from pymongo import MongoClient
# from json import loads
#
#
# consumer = KafkaConsumer(
#     'KAFKA_T',
#      bootstrap_servers=['localhost:9092'],
#      auto_offset_reset='earliest',
#      enable_auto_commit=True,
#      auto_commit_interval_ms = 500,
#      value_deserializer=lambda x: loads(x.decode('utf-8')))
#
#
# client = MongoClient('localhost:27017')
# collection = client.KAFKA_T.KAFKA_TOPIC
#
# for message in consumer:
#     try:
#         print(message.value)
#         message = message.value
#         collection.insert_one(message)
#     except:
#         print("Breaking the for loop coz of invalid message")
#         break
#     print('{} added to {}'.format(message, collection))
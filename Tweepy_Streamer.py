import json
import bson
from bson import json_util

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

for i in range(10):
    data = (parsed.json)   
    producer.send('orders', json.dumps(d, indent=4, default=json_util.default).encode('utf-8'))
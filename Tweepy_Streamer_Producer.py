# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 00:48:39 2018

@author: yasha
"""
import tweepy
import time
from kafka import KafkaProducer

import twitter_Credientials
auth: OAuthHandler = OAuthHandler(twitter_Credientials.CONSUMER_KEY, twitter_Credientials.CONSUMER_SECRET)
auth.set_access_token(twitter_Credientials.ACCESS_TOKEN, twitter_Credientials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def normalize_timestamp(time):
    mytime = datetime.strftime(time, "%Y-%m-%d %H:%M:%S")
    mytime += timedelta(hours=1)
    return (mytime.strfttime("%Y-%m-%d %H:%M:%S"))

#defining Kafka Producer
producer = KafkaProducer(bootstrap_servers = 'localhost:2181')
topic_name = 'tweets-lambda1'

def get_twitter_data():
    res =api.search('Apple or iphone or iPhone')
    for i in res:
        record = ''
        record += str(i.user.id_str)
        record = ';'
        record += str(normalize_timestamp(str(i.created_at)))
        record = ';'
        record += str(i.user.followers_count)
        record = ';'
        record += str(i.user.location)
        record = ';'
        record += str(i.favorite_count)
        record = ';'
        record += str(i.retweet_coount)
        record = ';'
        producer.send(topic_name, str.encode(record))

get_twitter_data()

def periodic_work(interval):
    while True:
        get_twitter_data()
        time.sleep(5)




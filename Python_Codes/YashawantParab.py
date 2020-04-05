# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 00:05:08 2019

@author: yasha
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pymongo import MongoClient
import matplotlib.pyplot as plt
import json

plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (6, 4)
#matplotlib inline

color = sns.color_palette()
import warnings
warnings.filterwarnings('ignore') 

df_train =  MongoClient('localhost:27017')
db = df_train.Taxi
collection = df_train.Taxi.TaxiJan
df_train.dtypes


df_train.describe()
print('Old size: %d' % len(df_train))
df_train = df_train[df_train.fare_amount>=0]
print('New size: %d' % len(df_train))

df_train[df_train.fare_amount<100].fare_amount.hist(bins=100, figsize=(14,3))
plt.xlabel('fare $USD')
plt.title('Histogram');




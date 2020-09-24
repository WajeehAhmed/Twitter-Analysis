# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 02:27:49 2020

@author: Wajeeh Ahmed
"""


#Libraries Import
import pandas as pd
import requests
from bs4 import BeautifulSoup 
import seaborn as sns
import matplotlib.pyplot as plt

#load the scrap dataset
dataset = pd.read_csv('D:\Scripting\Professional Projects\Tweets_stats.csv')

sns.barplot(x='Followers',y='DisplayName',data = dataset[5:])

sns.boxplot(x= 'Followers',y ='DisplayName',data= dataset[5:])

correlation = dataset.corr()
sns.heatmap(correlation)
sns.pairplot(correlation)


plt.pie(dataset['Followers'],labels=dataset['DisplayName'],autopct='%1.2f',startangle=90)
plt.axis('equal')
plt.show()

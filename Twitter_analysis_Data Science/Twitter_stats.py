from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#import xlsxwriter 
import time
import re 
import pandas as pd
browser = webdriver.Chrome('C:/chromedriver_win32/chromedriver')
browser.maximize_window()
browser.get('https://socialblade.com/twitter/')
time.sleep(5)
Rank = []
Grade = []
UserName = []
DisplayName = []
Tweets = []
Followers = []
Following = []
for i in range(10,34):
    Rank.append(browser.find_element_by_xpath('/html/body/div[13]/div[1]/div['+str(i)+']/div[1]').text)
    Grade.append(browser.find_element_by_xpath('/html/body/div[13]/div[1]/div['+str(i)+']/div[2]').text)
    UserName.append(browser.find_element_by_xpath('/html/body/div[13]/div[1]/div['+str(i)+']/div[3]').text)
    DisplayName.append(browser.find_element_by_xpath('/html/body/div[13]/div[1]/div['+str(i)+']/div[4]').text)
    Tweets.append(float((browser.find_element_by_xpath('/html/body/div[13]/div[1]/div['+str(i)+']/div[5]').text).replace(',','')))
    Followers.append(int((browser.find_element_by_xpath('/html/body/div[13]/div[1]/div['+str(i)+']/div[6]').text).replace(',','')))
    Following.append(int((browser.find_element_by_xpath('/html/body/div[13]/div[1]/div['+str(i)+']/div[7]').text).replace(',','')))

#info = browser.find_element_by_xpath('/html/body/div[13]/div[1]/div[9]').text
#/html/body/div[13]/div[1]/div[33]/div[1]
#/html/body/div[13]/div[1]/div[33]/div[2]
df = pd.DataFrame(list(zip(Rank,Grade,UserName,DisplayName,Tweets,Followers,Following)),columns =['Rank','Grade','UserName','DisplayName','Tweets','Followers','Following'])
df.to_csv('Tweets_stats.csv',index = False)
#print(df)
'''  
print(Rank)
print(Grade)
print(Name)
print(Videos)
print(Subscriber)
print(Views)
'''
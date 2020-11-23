import requests, time, random
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
res=[]      #A list that will store the first result of google search
import time

#You need to make a csv file with column "Company Name" That will hold your search topic.
browser = webdriver.Chrome(r'C:\Users\akhil.damri\Downloads\chromedriver_win32\chromedriver.exe') #Address to the chrome driver
temp = pd.read_csv('CompanyList.csv') #Address of CSV having List of company name or google search
flag=1
for i in temp['Company Name']:
    print("Working on ", flag,"row")
    #i=str(i).split('-')[0].strip()
    search_string=i
    search_string = search_string.replace(' ', '+')
    for i in range(1):
        matched_elements = browser.get("https://www.google.com/search?q=" + search_string + "&start=" + str(i))

    content = browser.page_source
    soup = BeautifulSoup(content)
    count=0
    for div in soup.findAll('div', attrs={'class':'yuRUbf'}):
        for a in div.find_all('a', href=True):
            if(count==0):
                res.append(a['href'])
                print ("Found the URL:", a['href'])
            count=1
    flag=flag+1
    time.sleep(1)
    
#Appending the result to the dataframe temp and exporting it
temp['google'] = res
temp.to_csv("resultWithoutdash.csv")
browser.close()
# you can also open the Result of search by using .click() function.

import requests, time, random
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
res=[]      #A list that will store the first result of google search


#You need to make a csv file with column "Company Name" That will hold your search topic.
browser = webdriver.Chrome('chromedriver.exe') #Address to the chrome driver
temp = pd.read_csv('scrapingTest.csv') #Address of CSV having List of company name or google search


for i in temp['Company Name']:
    #i=str(i).split('-')[0].strip()
    search_string=i
    search_string = search_string.replace(' ', '+')
    for i in range(1):
        matched_elements = browser.get("https://www.google.com/search?q=" + search_string + "&start=" + str(i))

    #path2 is Xpath of the search you want to get
    # You have to modify it according to your required result.
    #you Can easily find xpath of any component using a chrome extension "Xpath finder"
    Path2="/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/a/div/cite"
    elem2=browser.find_elements_by_xpath(Path2)
    if(len(elem2)==0):
        res.append('NULL')
        print("NULL APPENDED")
        #Appending the null if it fails to get result
        #TO make this correct you need to give the xpath (Path2) correctly
        continue
    for elem1 in browser.find_elements_by_xpath(Path2):
        res.append(elem1.text)
        print(elem1.text)
#Appending the result to the dataframe temp and exporting it
temp['google'] = res
temp.to_csv("result1.csv")
browser.close()
# you can also open the Result of search by using .click() function.

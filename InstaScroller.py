import time
from selenium import webdriver
from lxml import html
from bs4 import BeautifulSoup as bs
import pandas as pd
import re

#Load web driver from selenium
#browser = webdriver.Firefox(executable_path='/home/james/Gecko')
browser = webdriver.Firefox()
urllist = ['https://www.instagram.com/cityofboston/',
          'https://www.instagram.com/jameshuessy/']
dfl = []
for tt in range(len(urllist)):
    #send said driver out to instagram
    browser.get(urllist[tt])
    #Write the selenium script to force its way to the 'true' bottom of the page
    lenOfPage = browser.execute_script('window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;')
    match = False
    testpage = []
    while(match == False):
        #tell the driver to scroll and hit the end to trigger the next page load
        lastCount = lenOfPage
        #sleep to allow the new page to load
        time.sleep(3)
        #Record that page's data
        fg = browser.page_source
        fg = bs(fg, 'html.parser')
        fg = fg.find('section').find_all('a')
        tls = []
        for zz in range(len(fg)):
            jj = fg[zz].attrs['href']
            if '/p/' in jj:
                tls +=[jj]
        #Append dummy list with that page's data
        testpage += bs(browser.page_source, 'html.parser')
        #Execute the scroll again
        lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        #Ensure that there aren't any more pages to get
        if lastCount==lenOfPage:
            match = True
    links = []
    for i in range(len(testpage)):
        p1 = testpage[i].find('section').find_all('a')
    
        for z in range(len(p1)):
            lt = p1[z].attrs['href']
            if '/p/' in lt:
                links += [lt]
    #create a non-duped list
    sl = list(set(links))
    #append non-duped list 
    dfl += sl

#create new dataframe to be saved as a csv locally
lk = pd.DataFrame({'URL':dfl})
lk.to_csv('Instapulls.csv')
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 19:49:22 2018

@author: cemre
"""
from bs4 import BeautifulSoup
import re
import requests
import pandas as pd
import time
import string
from datetime import datetime, timedelta
import datetime
from dateutil.parser import parse
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np


start_url = 'https://www.coindesk.com/?s=smart+contracts'
html      = requests.get(start_url)
soup      = BeautifulSoup(html.text, "html5lib")
txt = soup.find('div', {"class" : "category-content"})
dates = [d[16:-1]for d in re.findall('<time datetime="[0-9]{4}-[0-9]{2}-[0-9]{2}T',str(txt))]
dates

#######################
title = txt.h3.a.get('title')
author = txt.cite.a.text
link = txt.h3.a.get('href')

article = requests.get(link)
soup      = BeautifulSoup(article.text, "html5lib")
artxt = soup.find('div', {"class" : "single-content"})

translator = str.maketrans('', '', string.punctuation)
artxt = artxt.translate(translator).lower()

def is_eth(text):
    if 'ethereum' in text:
        return('In article ' + title + " the word etherium appears.")
    else:
        return('In article ' + title + " the word etherium does not appear.")
is_eth(artxt)

########################

temptitle = txt.find_all(class_='fade')


titles = []
for title in temptitle:
    titles.append(title.text)
    print(titles)

def remove_empty(input):
    output = []
    for value in input:
        if "\n" not in value:
            output.append(value)
    return output

titles = remove_empty(titles)

stamp = txt.find_all(class_='timeauthor')

dates = []
for date in stamp:
    dates.append(date.time.get("datetime"))
    print(dates)

authors = []
for author in stamp:
    authors.append(author.cite.a.text)
    print(authors)
    

links = []

for link in txt.findAll('a', attrs={'href': re.compile('https://www.coindesk.com/')}):
    links.append(link.get('href'))
    print(links)

#Checking duolicates in the links            
def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

links = remove_duplicates(links)


# Removing author links
def remove_authors(value):
    output = []
    for val in value:
        if 'https://www.coindesk.com/author/' not in val:
            output.append(val)
    return output

links = remove_authors(links)


def access_article(value):
    article = requests.get(value)
    soup_a = BeautifulSoup(article.text, "html5lib")
    return soup_a

def article_txt(soup):
    artxt = str(soup.find('div', {"class" : "single-content"}).text)
    translator = str.maketrans('', '', string.punctuation)
    artxt = artxt.translate(translator).lower()
    return(artxt)
    
def is_eth(text):
    if 'ethereum' in text:
        return 1
    else:
        return 0

is_eth(artxt)

eth = []
for link in links:
    article = access_article(link)
    text = article_txt(article)
    eth.append(is_eth(text))

#Initiate the csv file incl header
with open("Coindesk_Articles.csv",'w') as file:
        file.write("Date, Title, Author, Etherum, Link")
        file.write('\n')    
 
# write results into csv using a loop (you stoill have to implement the loop)
with open("Coindesk_Articles.csv",'a') as file:
    file.write( string containing containing comma seperated values that are supposed to be one row )
    file.write('\n')  
    
    
a = access_article(links[0])
b = article_txt(a)
is_eth(b)

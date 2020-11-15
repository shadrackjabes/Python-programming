#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 09:56:47 2020

@author: shadrack
"""
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
from pattern3 import web
from bs4 import BeautifulSoup
from collections import defaultdict

def fetching_html(url):
    html=requests.get(url).content
    return(html)
def parsing_html(html):    
    soup = BeautifulSoup(html, 'html.parser')
    return(soup)
def fetching_table(soup,index):
    table=soup.find_all('table',{'class':'sortable wikitable'})[index]
    return(table)
def table_data(table):
    key=[i for i in range(len(table.find_all("tr")[0].find_all("th")))]
    
    value=[]    
    value_h=[table.find_all("tr")[0].find_all("th")[i].get_text(" ",strip=True) for i in range(len(table.find_all("tr")[0].find_all("th")))]    
    value.append(value_h)
    start=0
    ncols=len(table.tbody.find_all("tr")[1].find_all("td"))
    nrows=len(table.tbody.find_all("tr"))
    
    for i in range(start+1,nrows):
        value1=[]
        for j in range(start,ncols):
            value1.append(table.tbody.find_all("tr")[i].find_all("td")[j].get_text(" ",strip=True))
        value.append(value1)
    return(key,value)
def table_2_dictionary(key,value):
    tdict = {key[i]: value[i] for i in range(len(key))}
    return(tdict)
def dictionary_2_dataframe(tdict):
    df=pd.DataFrame(tdict)
    return(df)
    
url='http://en.wikipedia.org/wiki/List_of_countries_by_past_and_future_population'
html=fetching_html(url)
soup=parsing_html(html)
ntable=len(soup.find_all('table',{'class':'sortable wikitable'}))
for i in range(ntable):
    table=fetching_table(soup,i)
    key,value=table_data(table)
    tab2dict=table_2_dictionary(key,value)
    dict2dframe=dictionary_2_dataframe(tab2dict)
    print(pd.transpose(dict2dframe.set_index(0).head()))

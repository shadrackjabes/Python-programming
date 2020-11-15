#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 10:22:06 2020

@author: shadrack
"""
import pandas as pd
import numpy as np
import re
import requests
from pattern3 import web
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def get_poll_xml(poll_id):    
    """
Function
--------
get_poll_xml

Given a poll_id, return the XML data as a text string

Inputs
------
poll_id : int
    The ID of the poll to fetch

Returns
-------
xml : str
    The text of the XML page for that poll_id

Example
-------
>>> get_poll_xml(1044)
u'<?xml version="1.0" encoding="UTF-8"?><chart><series><value xid=\'0\'>1/27/2009</value>
...etc...
    """
    url = "http://charts.realclearpolitics.com/charts/" + str(poll_id) + ".xml"
    xml=requests.get(url).content
    return(xml)    

def rcp_poll_data(xml):
    """
    Function
    ---------
    rcp_poll_data

    Extract poll information from an XML string, and convert to a DataFrame

    Parameters
    ----------
    xml : str
        A string, containing the XML data from a page like 
        get_poll_xml(1044)
        
    Returns
    -------
    A pandas DataFrame with the following columns:
        date: The date for each entry
        title_n: The data value for the gid=n graph (take the column name from the `title` tag)
        
    This DataFrame should be sorted by date
        
    Example
    -------
    Consider the following simple xml page:
    
    <chart>
    <series>
    <value xid="0">1/27/2009</value>
    <value xid="1">1/28/2009</value>
    </series>
    <graphs>
    <graph gid="1" color="#000000" balloon_color="#000000" title="Approve">
    <value xid="0">63.3</value>
    <value xid="1">63.3</value>
    </graph>
    <graph gid="2" color="#FF0000" balloon_color="#FF0000" title="Disapprove">
    <value xid="0">20.0</value>
    <value xid="1">20.0</value>
    </graph>
    </graphs>
    </chart>
    
    Given this string, rcp_poll_data should return
    result = pd.DataFrame({'date': pd.to_datetime(['1/27/2009', '1/28/2009']), 
                           'Approve': [63.3, 63.3], 'Disapprove': [20.0, 20.0]})   
    """
    soup=BeautifulSoup(xml,'html.parser')
    table=soup.chart
    #create keys
    keys=['date']
    data=[]
    nrows=len(table.series.find_all("value"))
    data.append([table.series.find_all("value")[i].get_text(" ",strip=True) for i in range(nrows)])
    #create values
    ngraphs=len(table.graphs.find_all("graph"))
    for i in range(ngraphs):
        keys.append(table.graphs.find_all("graph")[i]["title"])
        data.append([table.graphs.find_all("graph")[i].find_all("value")[j].get_text(" ",strip=True) for j in range(nrows)])
    #create dictionaries        
    value=[]
    value=zip(keys,data)
    table_dictionary=dict(value)
    #create daraframes
    dframe=pd.DataFrame(table_dictionary)
    return(dframe)

for i in df.columns:
    x = df.date.map(lambda x:x.split('/')[-1])
    y=df[i]
    print(x,y)
    
    
#fig,axes=plt.subplots(figsize=(5,5))
#axes.plot(x,y)
#fig.tight_layout()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 21:33:28 2020

@author: shadrack
"""
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
from pattern3 import web
from bs4 import BeautifulSoup
from collections import defaultdict

def get_poll_xml(ind):
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
    xml="http://charts.realclearpolitics.com/charts/"+ str(ind) +".xml"
    retrive=requests.get(xml).text
    return(retrive)

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
    soup = BeautifulSoup(xml, 'html.parser')
    date=[]
    title=[]
    title_value=[]
    for i in range(len(soup.chart.series)):
        date.append(soup.chart.series.value.get_text(" ",strip=True))
        for i in range(len(soup.graphs)):
            title.append(soup.graphs.find_all("graph")[i]["title"])
            title_value.append(soup.graphs.find_all("graph")[i].get_text(" ",strip=True))
            
    dicts = {}
    dicts['date'] = pd.to_datetime(date)
    for i in range(len(title)):
        dicts[title[i]] = title_value[i]
    return(pd.DataFrame(dicts))

#xml=get_poll_xml(1171)
#data=rcp_poll_data(xml)
#print(data)



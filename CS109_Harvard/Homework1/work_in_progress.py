#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 10:22:06 2020

@author: shadrack
"""
import pandas as pd
import numpy as np
import requests
import re
from pattern3 import web
from bs4 import BeautifulSoup

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
    xml = "http://charts.realclearpolitics.com/charts/" + str(poll_id) + ".xml"
    html=requests.get(xml).content
    return(html)    

def rcp_poll_data(html):
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
    soup=BeautifulSoup(html,'html.parser')
    table=soup.chart
    
    keys=['date']
    data=[]
    nrows=len(table.series.find_all("value"))
    data.append([table.series.find_all("value")[i].get_text(" ",strip=True) for i in range(nrows)])
    
    ngraphs=len(table.graphs.find_all("graph"))
    for i in range(ngraphs):
        keys.append(table.graphs.find_all("graph")[i]["title"])
        data.append([table.graphs.find_all("graph")[i].find_all("value")[j].get_text(" ",strip=True) for j in range(nrows)])
        
    value=[]
    value=zip(keys,data)
    table_dictionary=dict(value)
    
    df=pd.DataFrame(table_dictionary)
    return(df.set_index('date'))
    
def get_pollurl_list(url):   
    """
    Function
    --------
    find_governor_races

    Find and return links to RCP races on a page like
    http://www.realclearpolitics.com/epolls/2010/governor/2010_elections_governor_map.html
    
    Parameters
    ----------
    html : str
        The HTML content of a page to scan
        
    Returns
    -------
    A list of urls for Governer race pages
    
    Example
    -------
    For a page like
    
    <html>
    <body>
    <a href="http://www.realclearpolitics.com/epolls/2010/governor/ma/massachusetts_governor_baker_vs_patrick_vs_cahill-1154.html"></a>
    <a href="http://www.realclearpolitics.com/epolls/2010/governor/ca/california_governor_whitman_vs_brown-1113.html"></a>
    </body>
    </html>
    
    find_governor_races would return
    ['http://www.realclearpolitics.com/epolls/2010/governor/ma/massachusetts_governor_baker_vs_patrick_vs_cahill-1154.html',
     'http://www.realclearpolitics.com/epolls/2010/governor/ca/california_governor_whitman_vs_brown-1113.html']
    """
    html=requests.get(url).content
    soup=BeautifulSoup(html,'html.parser')
    ntr = soup.tbody.find_all("tr")
    l=[[ntr[i].find_all("td")[j].a for j in range(len(ntr[i].find_all("td")))] for i in range(len(ntr))]           
    return(l)
    
url = "http://www.realclearpolitics.com/epolls/2010/governor/2010_elections_governor_map.html"
tablefile=get_pollurl_list(url)
print(tablefile)
    


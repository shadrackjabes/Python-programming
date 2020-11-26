#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 22:19:09 2020

@author: shadrack
"""
import requests
from bs4 import BeautifulSoup

def fetching_html(url):
    html=requests.get(url).content
    return(html)
def parsing_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    return(soup)
def get_movie(soup):
    title=[]
    tag_body=soup.find_all('body')
    for i in range(len(tag_body)):
        tag_h3=tag_body[i].find_all('h3')
        tag_div=tag_body[i].find_all('div',{'class':'inline-block ratings-imdb-rating'})
        for j in range(len(tag_h3)):
            tag_a=tag_h3[j].find_all('a',href=True)
            for k in range(len(tag_a)):
                title.append(tag_a[k].get_text(" ",strip=True))
        #for j in range(len(tag_div)):
            #rating.append(tag_div[j].find("strong").get_text(" ",strip=True))
    return(title)

 
url='http://www.imdb.com/search/title?sort=num_votes,desc&start=1&title_type=feature&year=1950,2012'
html=fetching_html(url)
soup=parsing_html(html)
title=get_movie(soup)
print(title)





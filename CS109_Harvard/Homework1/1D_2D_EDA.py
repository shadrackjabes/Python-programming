#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 10:32:13 2020

@author: shadrack
"""
import pandas as pd
import matplotlib.pyplot as plt

# read from file
df=pd.read_csv("olive.csv")
# rename column appropriately
repl={df.columns[0]:'areanames'}
df.rename(columns=repl,inplace=True)

#1D data explore
# collect acidlist and its extremas
acidlist=df.columns[3:]
nbins=100
data={}
for ind,i in enumerate(acidlist):
    bw=(df[i].max()-df[i].min())/nbins
    g=np.zeros(nbins)
    x=np.linspace(df[i].min(),df[i].max(),nbins)
    norm = 0
    for j in range(len(df[i])):
        
        val=df[i].iloc[j]-df[i].min()
        ib=int(val/bw)+1
        if(ib<nbins):
            g[ib]=int(g[ib])+1
            norm = norm + 1
    
    data=[g[k]/norm for k in range(nbins)]
    #plt.scatter(x,data)
    #plt.show()

# 2D data explore
for k,v in df.groupby('Region'):
    #print(k,v)
    for ind_l,l in enumerate(acidlist):
        for ind_m,m in enumerate(acidlist):
            if(ind_l>ind_m):
                plt.scatter(v[l],v[m])
                plt.xlabel(l)
                plt.ylabel(m)
                plt.title('region'+str(k))
                plt.show()

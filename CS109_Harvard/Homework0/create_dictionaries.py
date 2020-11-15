#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 12:00:31 2020

@author: shadrack
"""
import numpy as np
import pandas as pd

key=['col1','col2','col3','col4']
value=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

result=zip(key,value)
result_list=dict(result)

df=pd.DataFrame(result_list)
#print(df)


#print(np.random.randn(10,2))
plot_df = pd.DataFrame(np.random.randn(10,2),columns=['x','y'])

#print(plot_df)

print(plot_df.iloc[1,:])


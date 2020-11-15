# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt  

nexp=1000
nflips=25
nbin = 100
p=np.zeros(nbin)
delbin = 1/nbin
norm = 0
cnt = 0

for j in range(nexp):
    cnt += 1
    cnt_head = 0
    
    for i in range(nflips):
        A = np.random.rand(1)
        if(A > 0.5):
            head = 1
        else:
            head = 0
        cnt_head = cnt_head + head
        
    val = cnt_head/nflips
    ibin = int(val/delbin)
    p[ibin] = p[ibin] + 1
    norm = norm + 1
  
x=[i*delbin for i in range(nbin)]
y=[p[i]/norm for i in range(nbin)]
fig,axes=plt.subplots(nrows=1,ncols=1,figsize=(5,5))
axes.plot(x,y)        
        

    
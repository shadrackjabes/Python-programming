#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 11:12:34 2020

@author: shadrack
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# loading dataset
df=pd.read_csv(url)
df.columns=['sepal length','sepal width','petal length','petal width','target']
#print(df.columns)

#standardization method 1
x_variables=['sepal length','sepal width','petal length','petal width']
y_variables=['target']
y=df[y_variables]
x=df[x_variables]
avg=df.mean(axis=0)
std=df.std(axis=0)
xnorm = (x-avg)/std
#print(xnorm)
# standardization method 2
#sc= StandardScaler()
#scale = sc.fit_transform(x) 
#print(scale)

# PCA
pcamodel=PCA(n_components=3)
pcomponents=pcamodel.fit_transform(xnorm)
# tabulate principal components
pcdf=pd.DataFrame(data=pcomponents,columns=['pc1','pc2','pc3'])
pcdf_total=pd.concat([pcdf,df['target']],axis=1)
print(pcdf_total)
#print(df['target'])
#print(pcdf)

# visualize PCA
fig,axes=plt.subplote(figsize=(4,4))
colors=['r','b','g']
targetnames=['Iris-setosa','Iris-versicolor','Iris-virginica']
for i in t,c zip(targetnames,colors):
    pcdf_total.loc[ ['target']=targetnames],[pc1]



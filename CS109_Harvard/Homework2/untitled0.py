#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 12:19:40 2020

@author: shadrack
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

states_abbrev_dict = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}
abbrev_states_dict = {v: k for k, v in states_abbrev_dict.items()}

#reading 
census_data = pd.read_csv("./data/census2010.csv")
#maping
def abbrev(key):
    k=key.title()
    value=abbrev_states_dict.get(k)
    return(value)
#print(census_data['state'])
census_data['state']=census_data['state'].map(abbrev)
#print(census_data)

# plotting columns and its correlation
sel=['educ_coll', 'average_income', 'per_vote']
#fig,axes =plt.subplots(nrows=3,ncols=3,figsize=(4,4))
#for i in range(len(sel)):
#    for j in range(len(sel)):
#        axes[i][j].scatter(census_data[sel[i]],census_data[sel[j]])
#fig.tight_layout()

# linear regression
smaller_frame=census_data[sel]
X_HD=smaller_frame[['educ_coll', 'average_income']].values
X_HDn=(X_HD - X_HD.mean(axis=0))/X_HD.std(axis=0)
educ_coll_std_vec=X_HDn[:,0]
#educ_coll_std=educ_coll_std_vec.reshape(-1,1)
print(X_HDn[:,0].reshape(-1,1))




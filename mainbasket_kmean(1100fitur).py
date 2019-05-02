# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:15:07 2019

@author: Hilmi
"""

import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

data = pd.read_csv('hilmi_baru.csv', index_col=0, encoding="utf-8", sep=';')
# print(data.info())
# print(data.head())


import numpy as np
import csv
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

filename = "hilmi_baru.csv"

path_dir = ".\\"
dataframe = pd.read_csv('hilmi_baru_tfidv.csv', encoding='utf-8', skiprows=0, index_col=0, sep=',')

df = dataframe.copy(deep=True)

banyak_cluster = list(range(2, 150))
print ("Kmeans kluster dari 2 to 149: ", banyak_cluster)

temp=[]
temp_pred=[]
for n_cluster in banyak_cluster:
    clusterer = KMeans(n_clusters=n_cluster)
    preds = clusterer.fit_predict((df))
    centers = clusterer.cluster_centers_
    score = silhouette_score(df, preds, metric='euclidean')
    temp.append(score)
    temp_pred=[]

    print ("Untuk kluster={},silhoute score :{} ".format(n_cluster, repr(score)))
    print(preds)

print ("kluster terbaik")
print ("kluster ke > "+str(temp.index(max(temp))+2)+" >silhout> "+str(max(temp)))

print (banyak_cluster)
print (temp)

baru=pd.DataFrame(columns=['kluster','silhout'])
baru['kluster']=banyak_cluster
baru['silhout']=temp

print (baru.head())

baru.to_csv('klustering_1099fitur.csv')

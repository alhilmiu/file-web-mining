import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import math
data = pd.read_csv('mainbasket_vsmsatufitur.csv', index_col=0, encoding="utf-8", sep=',')
list_fitur=data.keys().to_list()

w=[]
for i in list_fitur:

    a=data[i].value_counts()
    a=float(len(list_fitur)-a[0])
    #temp=math.log((len(list_fitur)-1)/(a))
    temp = math.log(len(list_fitur) / (a)) + 1
    w.append(temp)

print (data.head())
count=0
for i in range(len(list_fitur)):
    temp=list_fitur[i]
    data[temp]*=w[i]
print (data.head())

data.to_csv('baru_tfidf.csv')

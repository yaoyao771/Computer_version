#coding:utf-8
import math
from numpy import *

def createdataset():
    data=array([[1.0,2.0],[1.2,0.1],[0.1,1.4],[0.3,3.5]])
    labels=['A','A','B','B']
    return data,labels
def classify(input,dataset,label,K):
    data_size=dataset.shape[0]
    distance_diff=tile(input,(data_size,1))-dataset
    distance=distance_diff**2
    sum_dim=sum(distance,axis=1)
    sum_sqrt=sum_dim**0.5
    sort_index=argsort(sum_sqrt)

    count={}
    for i in range(K):
       datalabel=label[sort_index[i]]

       count[datalabel]=count.get(datalabel,0)+1
    maxcount=0
    for key,value in count.items():
        if value>maxcount:
            maxvalue=value
            classes=key
    return classes


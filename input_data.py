#coding:utf-8
import sys
import KNN
from numpy import *
dataset,label=KNN.createdataset()
input=array([1.1,1.3])
K=3
output=KNN.classify(input,dataset,label,K)
print("test_data",input,"answer",output)
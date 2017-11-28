#encoding：utf-8
from numpy import *
def lossfun(X_train,Y_train,L):
    bestloss=float("inf")
    for num in range(1000):
        W=np.random.randn(10.3073)*0.0001
        loss=L(X_train,Y_train,W)
        if loss<bestloss:
            bestloss=loss
            bestW=W
        print ("inattempt %d the loss was %f,best %f"%(num,loss,bestloss))
def L(W,X_train,Y_train):
    gradient=
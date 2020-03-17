import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
def eucledian(a,b):
    t=(a[0]-b[0])**2 + (a[1]-b[1])**2
    t=math.sqrt(t)
    return(t)
def centroid_val(l):
    s1=0.0
    s2=0.0
    for i in l:
        s1=s1+i[0]
        s2=s2+i[1]
    s1=s1/len(l)
    s2=s2/len(l)
    return([s1,s2])
data=pd.read_csv("D:\data-mining\ipl.csv")
c1=[]
c2=[]
data=data.values.tolist()
centroid1=data[0]
centroid2=data[1]
for i in data:
    if eucledian(centroid1,i) <eucledian(centroid2,i):
        c1.append(i)
    else:
        c2.append(i)
centroid1=centroid_val(c1)
centroid2=centroid_val(c2)
for i in range(1,500):
    t1=[]
    t2=[]
    for j in c1:
        if eucledian(centroid1,j)< eucledian(centroid2,j):
            t1.append(j)
        else:
            t2.append(j)
    for j in c2:
        if eucledian(centroid1,j)< eucledian(centroid2,j):
            t1.append(j)
        else:
            t2.append(j)
    c1=t1
    c2=t2
    centroid1=centroid_val(c1)
    centroid2=centroid_val(c2)

x=[]
y=[]
for i in c1:
    x.append(i[0])
    y.append(i[1])
plt.scatter(x,y)
x=[]
y=[]
for i in c2:
    x.append(i[0])
    y.append(i[1])
plt.scatter(x,y,color="g")
plt.scatter(centroid1[0],centroid1[1],marker="x")
plt.scatter(centroid2[0],centroid2[1],marker="x")
plt.show()
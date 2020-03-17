import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
data=pd.read_csv("D:\\data-mining\\train.csv")
x1=data["BedroomAbvGr"].values
x2=data["GrLivArea"].values
y=data["SalePrice"].values
X=[]
for i in range(0,len(x1)):
    X.append([1,x1[i],x2[i]])
X=np.array(X)
Y=np.array(y)
theta=np.linalg.inv(X.transpose().dot(X)).dot(X.transpose().dot(Y))
print(theta)
ax = plt.axes(projection="3d")
ax.scatter3D(x1, y, x2,c="g")
plt.xlabel("No of bedrooms")
plt.show()
bed=int(input("Enter no of bedrooms"))
area=int(input("Enter area"))
p=np.array([1,bed,area]).dot(theta)
print("The price of house is",p)
import csv
import matplotlib.pyplot as plt
x=[]
y=[]
with open ('train.csv','r') as file:
    reader=csv.reader(file)
    c=0
    for row in reader:
        if c==0:
            c=c+1
            continue
        x.append(int(row[46]))
        y.append(int(row[80]))
        c=c+1
        if c==201:
            break
print(x)
print(y)
plt.scatter(x,y)
plt.xlabel("Area of house")
plt.ylabel("Cost of house")

xmean=0.0
ymean=0.0
for i in range(200):
    xmean=xmean+x[i]
    ymean=ymean+y[i]
xmean=xmean/200
ymean=ymean/200
p1=0.0
p2=0.0
for i in range(200):
    p1=p1+((x[i]-xmean)*(y[i]-ymean))
    p2=p2+((x[i]-xmean)**2)
m=p1/p2
print("The equation of line is y=",m,"x+",c)
yp=[]
xp=[]
for i in range(min(x),max(x)):
    yp.append(m*i+c)
    xp.append(i)
plt.scatter(xp,yp,color="r")
plt.title("Equation of line : y="+str(m)+"x+"+str(c))
plt.show()
pr=int(input("Enter area"))
print("The predicted price is ",pr*m+c)
import numpy as np
import matplotlib.pyplot as plt
x=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.array([1,3,2,5,7,8,8,9,10,12])
n=np.size(x)
mx=np.mean(x)
my=np.mean(y)
mxy=np.sum(x*y)-n*mx*my
mxx=np.sum(x*x)-n*mx*mx
b=mxy/mxx
a=my-b*mx
ypred=a+b*x
plt.scatter(x,y)
plt.plot(x,ypred)
plt.show()

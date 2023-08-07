import numpy as np
import matplotlib.pyplot as plt
x=[1,3,5,6,7,8,9,0,12,13,14,15,16,18,20,21,22]
y=[100,99,98,80,60,60,55,65,70,75,76,78,79,90,99,99,100]
m=np.poly1d(np.polyfit(x,y,3))
ml=np.linspace(1,22,100)
plt.scatter(x,y)
plt.plot(ml,m(ml))
plt.show()

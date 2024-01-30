import matplotlib.pyplot as plt 
import numpy as np 

x=np.array([1,7,5,3,2,40])
y=np.array([50,120,10,30,80,200])
boyut=np.array([y[0],y[1],y[2],y[3],y[4],y[5]])
plt.scatter(x,y,s=boyut)
plt.show()
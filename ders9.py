import matplotlib.pyplot as plt 
import numpy as np 

x=np.array([0,1,2,3])
y=np.array([3,8,1,10])
plt.subplot(1,3,1)
plt.plot(x,y)


x=np.array([0,1,2,3])
y=np.array([13,11,10,15])
plt.subplot(1,2,2)
plt.plot(x,y)
x=np.array([0,1,2,3,4])
y=np.array([13,11,4,15,10])
plt.subplot(1,3,3)
plt.plot(x,y)
plt.show()
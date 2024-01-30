import numpy as np 
import matplotlib.pyplot as plt 

x=np.array([0,1,2,3,4,5])
y=np.array([5,15,1,10,3,20])
x2=np.array([0,1,2,3,4,5])
y2=np.array([1,4,8,2,10,3])
x3=np.array([0,1,2,3,4,5])
y3=np.array([1,4,9,16,25,36])

plt.plot(x,y,x2,y2,x3,y3,marker='o')
plt.show()

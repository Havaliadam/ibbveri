import numpy 
import matplotlib.pyplot as plt 
from numpy import random
x=[]
y=[]

for a in range(20):
    y.append(random.randint(10))
    x.append(a)
x1=numpy.array(x)
y1=numpy.array(y)
plt.plot(x1,y1)
plt.show()    
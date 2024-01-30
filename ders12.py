import matplotlib.pyplot as plt 
import numpy as np 

ort1=int(input("1.ortalama:"))
ort2=int(input("2.ortalama:"))
ort3=int(input("3.ortalama:"))
ort4=int(input("4.ortalama:"))

x=np.array(["1.ortalama","2.ortalama","3.ortalama","4.ortalama"])
y=np.array({ort1,ort2,ort3,ort4})


plt.bar(x,y)
plt.show()
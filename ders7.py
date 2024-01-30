import numpy as np 
import matplotlib.pyplot as plt 

x1=np.array([1,2,3,4,5,6])
y1=np.array([5,6,12,25,1,5])

plt.title("grafik başlıgı",loc="left")#başlık adş loc başlıgı yer bildirir
plt.xlabel("x etiket")
plt.ylabel("y etiket")
plt.plot(x1,y1)
plt.show()

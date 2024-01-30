import matplotlib.pyplot as plt 
import numpy as np 


etiket=np.array(["a","b","c","d"])
yuzdedeger=np.array([30,15,15,40])
enbuyuk=[0,0,0,0.3]
plt.pie(yuzdedeger,labels=etiket)
plt.show()
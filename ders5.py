import matplotlib.pyplot as plt 
import numpy as np 

# x=np.array([1,5,7,10,15,8])
y=np.array([5,15,1,20,8,10,4])

plt.plot(y,'o-r',ms=10,mec='#454143',mfc='#454143')#atama marker işaretleme yapar
#*--r kırmızı ve çizgi yapar
plt.show()#gösterme
#'*' bu şekilde noktalama işaretleri gösteriri ms yıldız olarak gösterir

#mfc çizgi içerisndeki noktaları iç rengi değiştiri


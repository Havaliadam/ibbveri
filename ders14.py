import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib.animation as animation

figure, grafik1 = plt.subplots()
grafik1.set_xlim([0, 10])

scat = grafik1.scatter(0, 0)
scat2 = grafik1.scatter(0, 1)
grafik = np.linspace(0, 10, 200)

def animate(i):
    scat.set_offsets((grafik[i], 0))
    scat2.set_offsets((grafik[i], 1))
    print(i)
    return scat, scat2

animasyon = animation.FuncAnimation(figure, animate, repeat=True, frames=len(grafik), interval=20)

plt.show()

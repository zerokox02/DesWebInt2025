import matplotlib.pyplot as plt
import numpy as np
 
#x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
#y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
 
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
 
xhist = np.random.normal(170, 10, 250)
 
#Gráfica de lineas
#plt.plot(x, y)
#Gráfica de dispersión
#plt.scatter(x, y)
#Gráfica de barras
#plt.bar(x,y)
#Histograma
plt.hist(xhist)
plt.show()
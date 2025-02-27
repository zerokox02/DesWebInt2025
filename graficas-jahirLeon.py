import matplotlib.pyplot as plt
import numpy as np

#x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
#y = np.array([99,86,87,88,100,86,103,87,94,78,77,85,86])

#x = np.array(["A","B","C","D"])
#y = np.array([3,8,1,10])



xhist = np.random.normal(170, 10, 250)

#Grafica lineas
#plt.plot(x, y)
#Graficas de dispersión
#plt.scatter(x, y)
#Grafica de barras
#plt.bar(x, y)
#histograma
plt.hist(xhist)
plt.show()
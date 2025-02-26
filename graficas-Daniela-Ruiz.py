import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
ypoints = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

# Grafica de lienas
# plt.plot(x,   y)


#Grafica de dispersion
# plt.scatter(x, y)


#Grafica de barras
# x = np.array(["A", "B",  "C", "D"])
# y = np.array([3,8,1,10])
# plt.bar()


#Histograma
xhist = np.random.normal(170, 10, 250)
plt.hist(xhist)


# 
plt.show()
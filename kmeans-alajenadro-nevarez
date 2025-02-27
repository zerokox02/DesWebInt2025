import matplotlib.pyplot as plt
from sklearn.cluster import KMeans 


x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

data = list(zip(x, y))
kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

new_x = 11
new_y = 22

new_point = [(new_x, new_y)]

prediction = kmeans.predict(new_point)
print("Predicted class is : ", prediction[0])

plt.scatter(x, y, c=kmeans.labels_ + prediction[0])
plt.show()
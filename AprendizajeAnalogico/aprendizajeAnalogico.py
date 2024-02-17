from sklearn.neighbors import NearestNeighbors
import numpy as np

X_Train = np.array([[1,2], [2,3], [3,4], [4,5], [5,6]])

X_Unknown = np.array([[1.5, 2.5], [3.5, 4.5]])

model = NearestNeighbors(n_neighbords=2)
model.fit(X_Train)

distances, indices = model.kneighbors(X_Unknown)

for i in range (len(X_Unknown)):
    print("Para la observacion", X_Unknown[i], "los vecinos mas cercanos son:", X_Train[indices[i]])
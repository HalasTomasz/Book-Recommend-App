from sklearn.neighbors import NearestNeighbors
import numpy as np
from numpy import dot
from numpy.linalg import norm
from scipy import spatial
import pandas as pd 

df_books_ratings = pd.read_csv('user_data_ML.csv', nrows=21)

X = df_books_ratings.to_numpy()
print(X)
for index in range(0,len(X)):
    for index2 in range(index+1,len(X)):
        result = spatial.distance.cosine(X[index], X[index2])
        print(index, "ma dystans do", index2, result)
K = 3
nbrs = NearestNeighbors(n_neighbors=K, metric='cosine', algorithm='brute').fit(X)
distances, indices = nbrs.kneighbors(X)
print(distances)
print(indices)
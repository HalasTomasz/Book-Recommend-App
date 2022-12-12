# Import the relevant packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
# Number of points of each cluster
MAXN = 40
# Normal distribution 
data = np.concatenate([1.2*np.random.randn(MAXN, 2), 
                   5 + 1.7*np.random.randn(MAXN, 2)])
data = np.concatenate([data, [8, 3] + 1.1*np.random.randn(MAXN, 2)])
df = pd.DataFrame(data={'x' : data[:,0], 'y' : data[:,1]})


# drop the class column in order to have only the features in df
new_df = df.copy()
# empty list for inertia values
inertia = []
for i in range(1,10):
    # instantiating a kmeans model with i clusters
    # init=kmeans++ is default
    kmeans = KMeans(n_clusters=i)
    
    # fitting the model to the data
    kmeans.fit(new_df)
    
    # appending the inertia of the model to the list
    inertia.append(kmeans.inertia_)
    
    # Knowing from the data that we have three samples distributions
    # let's save the inertia for the case k=3
    if i == 3:
        elbow = kmeans.inertia_
# creating a list with the number of clusters
number_of_clusters = range(1,10)
plt.plot(number_of_clusters, inertia)
plt.plot(3, elbow, 'red')
plt.legend()
plt.xlabel('Liczba klastrów')
plt.ylabel('Inercja')
plt.show()
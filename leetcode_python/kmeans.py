import numpy as np
 
class KMeans:
 
    def __init__(self, n_clusters=5, max_iter=300, random_state=42):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.random_state = random_state
 
    def fit(self, X):
        np.random.seed(self.random_state)
        initial = np.random.permutation(X.shape[0])[:self.n_clusters]
        self.cluster_centers_ = X[initial]
 
        for _ in range(self.max_iter):
            self.labels_ = [self._nearest(self.cluster_centers_, x) for x in X]
            indices = [[i for i, l in enumerate(self.labels_) if l == j]
                        for j in range(self.n_clusters)]
            X_by_cluster = [X[i] for i in indices]
            # update the clusters
            self.cluster_centers_ = [c.sum(axis=0) / len(c) for c in X_by_cluster]
        # sum of square distances from the closest cluster - WCSS
        self.inertia_ = sum(((self.cluster_centers_[l] - x)**2).sum()
                            for x, l in zip(X, self.labels_))
        return self
 
    def _nearest(self, clusters, x):
        return np.argmin([self._distance(x, c) for c in clusters])
 
    def _distance(self, a, b):
        return np.sqrt(((a - b)**2).sum())
 
    def predict(self, X):
        return self.labels_
 
    def transform(self, X):
        return [[self._distance(x, c) for c in self.cluster_centers_] for x in X]
 
    def fit_predict(self, X):
        return self.fit(X).predict(X)
 
    def fit_transform(self, X):
        return self.fit(X).transform(X)
 
    def score(self, X):
        return -self.inertia_
 
X = np.random.random((50, 10))
 
kmeans = KMeans(n_clusters=5, random_state=1)
kmeans.fit(X)
print(kmeans.inertia_)
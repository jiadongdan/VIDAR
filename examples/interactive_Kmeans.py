import sys
sys.path.append('..')

import numpy as np
from vidar import interactive_kmeans

rng = np.random.RandomState(0)
n_samples = 1000
cov = [[0.4, 0], [0, 0.4]]
X = np.concatenate([
    rng.multivariate_normal(mean=[-2, 0], cov=cov, size=n_samples), 
    rng.multivariate_normal(mean=[2, 0], cov=cov, size=n_samples),
    rng.multivariate_normal(mean=[0.3, 1], cov=cov, size=n_samples)
    ])

n_clusters = 2
app = interactive_kmeans(X, n_clusters)
app.show()
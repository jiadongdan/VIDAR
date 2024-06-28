import sys
sys.path.append('..')

import numpy as np
from vidar import interactive_PCA

rng = np.random.RandomState(0)
n_samples = 1000
cov = [[1, 0], [0, 1]]
X = np.concatenate([
    rng.multivariate_normal(mean=[-2, 0], cov=cov, size=n_samples), 
    rng.multivariate_normal(mean=[2, 0], cov=cov, size=n_samples)])


n_components = 1
app = interactive_PCA(X, n_components)
app.show()
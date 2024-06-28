import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.widgets import PolygonSelector
from sklearn.cluster import KMeans


def colors_from_lbs(lbs, colors=None):
    mpl_20 = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
              '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
              '#3397dc', '#ff993e', '#3fca3f', '#df5152', '#a985ca',
              '#ad7165', '#e992ce', '#999999', '#dbdc3c', '#35d8e9']

    if colors is None:
        colors = np.array(mpl_20)
    else:
        colors = np.array(colors)
    lbs = np.array(lbs) % len(colors)
    return colors[lbs]

class InteractiveKMeans:

    def __init__(self, fig, axes, X, n_clusters, **kwargs):
        self.fig = fig
        self.X = X
        self.ax_orig, self.ax_redim = axes
        self.n_clusters = n_clusters

        self.kmeans = KMeans(n_clusters=n_clusters, random_state=40, n_init="auto")
        self.labels = self.kmeans.fit_predict(X)
        self.centers = self.kmeans.cluster_centers_

        self.plot_figure() # plot the initial figure

        self.selector = PolygonSelector(self.ax_orig, 
                            onselect=self.onselect, 
                            props=dict(color='r', linestyle='', linewidth=3, alpha=0.6, label=f"Component")
                            )
        self.selector.verts = self.centers

    def onselect(self, verts):
        self.centers = np.array(verts)
        self.update_cluster()
        self.plot_figure()

    def update_cluster(self):
        self.kmeans.cluster_centers_ = np.array(self.centers, dtype=np.float64)
        self.labels = self.kmeans.predict(self.X) 

    def plot_figure(self):       
        self.ax_orig.clear()
        self.ax_orig.scatter(self.X[:, 0], self.X[:, 1], 
                            alpha=0.3, label="samples", 
                            c=colors_from_lbs(self.labels))
        self.ax_orig.scatter(self.centers[:,0], self.centers[:,1], 
                            s=50, c='black', edgecolors='r')
        self.ax_orig.set(
            aspect="auto", 
            title="Interactive K-means",
            xlabel="first feature",
            ylabel="second feature",
        )

        self.ax_redim.clear()
        class_name = ['class {0}'.format(i+1) for i in range(len(self.centers))]

        # update labels
        counts = [np.sum(self.labels==i) for i in range(len(self.centers))]
        
        self.ax_redim.bar(class_name, counts, label=class_name, color=colors_from_lbs(range(len(self.centers))))
        self.ax_redim.set(
            aspect="auto",
            title="Clustering results",
            xlabel="Main feature",
            ylabel="Number of samples",
        )
        self.fig.canvas.draw_idle()

    def show(self):
        plt.tight_layout()
        plt.show()

def interactive_kmeans(X, n_clusters=2, **kwargs):
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    app = InteractiveKMeans(fig, axes, X, n_clusters=n_clusters, **kwargs)
    return app
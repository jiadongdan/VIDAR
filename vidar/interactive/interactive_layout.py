import numpy as np
# from statistics import mode
import matplotlib.pyplot as plt
from scipy.stats import mode
from matplotlib.widgets import LassoSelector
from matplotlib.path import Path


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


def _update_mean_patch(ax, p, cmap):
    if ax.images:  # ax.images not empty
        ax.images[0].set_data(p)
        ax.images[0].set_cmap(cmap)
    else:
        ax.imshow(p, cmap=cmap)


class InteractiveCluster:

    def __init__(self, fig, pts, ps, lbs=None, **kwargs):
        self.fig = fig
        self.ax_cluster = fig.axes[0]
        self.ax_patch = fig.axes[1]

        if lbs is None:
            self.lbs_ = np.array([0] * len(pts))
        else:
            self.lbs_ = lbs
        self.colors = colors_from_lbs(self.lbs_)

        self.path_collection = self.ax_cluster.scatter(pts[:, 0], pts[:, 1], c=self.colors, **kwargs)
        self.ax_cluster.axis('equal')
        self.ax_patch.set_xlim(0 - 0.5, ps.shape[2] - 0.5)
        self.ax_patch.set_ylim(ps.shape[1] - 0.5, 0 - 0.5)

        self.pts = pts
        self.ps = ps

        self.ind = None
        self.pts_selected = None

        self.lbs = np.array(len(self.pts) * [-1])

        self.num_clusters = 0

        self.lasso = LassoSelector(self.ax_cluster, onselect=self.onselect)
        self.press = self.fig.canvas.mpl_connect("key_press_event", self.press_key)

    def onselect(self, event):
        path = Path(event)
        self.ind = np.nonzero(path.contains_points(self.pts))[0]
        if self.ind.size != 0:
            self.pts_selected = self.pts[self.ind]

            # get the mean patch
            p = self.ps[self.ind].mean(axis=0)
            _update_mean_patch(self.ax_patch, p, cmap='gray')
            self.fig.canvas.draw_idle()

    def press_key(self, event):
        if event.key == "enter":
            if self.ind.any():
                self.lbs[self.ind] = self.num_clusters
                self.num_clusters += 1
                print("One cluster has been selected.")


def interactive_clusters(pts, ps, lbs=None, **kwargs):
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    app = InteractiveCluster(fig, pts, ps, lbs, **kwargs)
    return app
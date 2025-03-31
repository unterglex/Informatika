import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

np.random.seed(228)
centers = [(2, 3), (7, 5), (3, 8)]
radii = [1, 1.5, 0.8]
n_points_per_cluster = 50

x, y = [], []
for i in range(3):
    theta = np.random.uniform(0, 2 * np.pi, n_points_per_cluster)
    r = radii[i] + np.random.normal(0, 0.1, n_points_per_cluster)
    x_cluster = centers[i][0] + r * np.cos(theta)
    y_cluster = centers[i][1] + r * np.sin(theta)
    x.extend(x_cluster)
    y.extend(y_cluster)

def k_means(x, y, k=3):
    points = np.array(list(zip(x, y)))
    centroids = points[np.random.choice(len(points), k, replace=False)]
    labels_history = []
    centroids_history = [centroids.copy()]

    max_iters = 100
    epsilon = 0.001

    while True:
        distances = np.sqrt(((points - centroids[:, np.newaxis]) ** 2).sum(axis=2))
        labels = np.argmin(distances, axis=0)
        labels_history.append(labels.copy())

        new_centroids = np.array([points[labels == i].mean(axis=0) for i in range(k)])

        if np.all(np.abs(new_centroids - centroids) < epsilon):
            break

        centroids = new_centroids
        centroids_history.append(centroids.copy())

    return labels_history, centroids_history


labels_history, centroids_history = k_means(x, y, k=3)

fig, ax = plt.subplots(figsize=(8, 6))
plt.subplots_adjust(bottom=0.25)

ax_slider = plt.axes([0.15, 0.1, 0.7, 0.03])
slider = Slider(ax_slider, 'Iteration', 0, len(labels_history) - 1,
                valinit=0, valstep=1, valfmt='%0.0f')

points = ax.scatter(x, y, c=labels_history[0], cmap='viridis', s=50, alpha=0.6)
cent = ax.scatter(centroids_history[0][:, 0], centroids_history[0][:, 1],
                  c='red', marker='x', s=200, linewidth=3)
ax.set_title(f'Iteration 0')

def update(val):
    iteration = int(slider.val)
    points.set_array(labels_history[iteration])
    cent.set_offsets(centroids_history[iteration])
    ax.set_title(f'Iteration {iteration}')
    fig.canvas.draw_idle()

slider.on_changed(update)
plt.show()
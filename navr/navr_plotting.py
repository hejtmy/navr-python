import matplotlib.pyplot as plt
import numpy as np


# accepts array of tuples or two separate arrays
# TODO - change it to 2xN matrix or Nx2 matrix
def plot_path(positions_x, positions_y):
    plt.plot(positions_x, positions_y)
    plt.show()


# helper for plotting speeds and positions etc.
def plot_value_in_time(times, values):
    plt.plot(times, values)
    plt.show()


def plot_positions_heatmap(positions_x, positions_y, size=(64, 64)):
    #TODO - need to normalise the outcome, it is far not that
    heatmap, xedges, yedges = np.histogram2d(positions_x, positions_y, bins=size, density=True)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    plt.clf()
    plt.title('Position heatmap')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.imshow(heatmap, extent=extent, cmap='RdYlBu_r')
    plt.show()
    return heatmap
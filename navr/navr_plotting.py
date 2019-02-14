import matplotlib.pyplot as plt


# accepts array of tuples or two separate arrays
def plot_path(positions_x, positions_y):
    plt.plot(positions_x, positions_y)
    plt.show()

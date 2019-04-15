import numpy as np


# calculates rolling distance between consecutive positions
def calculate_distances(positions):
    positions_shifted = np.roll(positions, 1, 0)
    distances = np.linalg.norm(positions - positions_shifted, axis=1)
    return distances

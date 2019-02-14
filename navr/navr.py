import numpy as np
import navr.navr_preprocessing as nprep
import navr.navr_plotting as nplot


class Navr:
    def __init__(self, pd_data):
        if check_data(pd_data):
            self.data = pd_data
        else:
            raise Exception('Columns not correct')
            return None

    @property
    def positions_x(self):
        return np.asanyarray(self.data['position_x'])

    @property
    def positions_y(self):
        return np.asanyarray(self.data['position_y'])

    def calculate_distances(self):
        positions = self.data[['position_x', 'position_y']].values
        distances = nprep.calculate_distances(positions)
        self.data['distance'] = distances
        return distances

    def calculate_speed(self):
        if 'distance' not in self.data.columns:
            self.calculate_distances()
        if 'timestamp_diffs' not in self.data.columns:
            self.calculate_time_diff()
        distances = np.asanyarray(self.data['distance'])
        timediffs = np.asanyarray(self.data['time_diff'])
        speeds = distances / timediffs
        self.data['speed'] = speeds
        return speeds

    def calculate_time_diff(self):
        timediffs = np.diff(np.asanyarray(self.data['timestamp']))
        timediffs = np.concatenate([[np.Inf], timediffs])
        self.data['time_diff'] = timediffs
        return timediffs

    # PLOTTING -----------------

    #
    def plot_path(self):
        nplot.plot_path(self.positions_x, self.positions_y)

    def plot_path_heatmap(self, size=(64, 64)):
        heatmap = nplot.plot_positions_heatmap(self.positions_x, self.positions_y, size=size)
        return heatmap


def check_data(pd_data):
    column_names = ['timestamp', 'position_x', 'position_y']
    return len(set(pd_data.columns) & set(column_names)) >= 3


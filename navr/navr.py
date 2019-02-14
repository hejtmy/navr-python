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

    @property
    def timestamps(self):
        return np.asanyarray(self.data['timestamp'])

    @property
    def distances(self):
        if 'distance' not in self.data.columns:
            positions = self.data[['position_x', 'position_y']].values
            distances = nprep.calculate_distances(positions)
            self.data['distance'] = distances
        return np.asanyarray(self.data['distance'])

    @property
    def time_diffs(self):
        if 'timestamp_diffs' not in self.data.columns:
            timediffs = np.diff(np.asanyarray(self.data['timestamp']))
            timediffs = np.concatenate([[np.Inf], timediffs])
            self.data['time_diff'] = timediffs
        return np.asanyarray(self.data['time_diff'])

    @property
    def speeds(self):
        if 'speed' not in self.data.columns:
            speeds = self.distances / self.time_diffs
            self.data['speed'] = speeds
        return np.asanyarray(self.data['speed'])

    # PLOTTING -----------------
    def plot_path(self):
        nplot.plot_path(self.positions_x, self.positions_y)

    def plot_path_heatmap(self, size=(64, 64)):
        heatmap = nplot.plot_positions_heatmap(self.positions_x,
                                               self.positions_y, size=size)
        return heatmap

    def plot_speeed(self):
        nplot.plot_value_in_time(self.timestamps, self.speeds)


def check_data(pd_data):
    column_names = ['timestamp', 'position_x', 'position_y']
    return len(set(pd_data.columns) & set(column_names)) >= 3


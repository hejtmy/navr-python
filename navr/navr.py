import pandas as pd
import numpy as np
import navr.navr_preprocessing as prep


class Navr:
    def __init__(self, pd_data):
        if check_data(pd_data):
            self.data = pd_data
        else:
            raise Exception('Columns not correct')
            return None

    def calculate_distances(self):
        positions = self.data[['position_x', 'position_y']].values
        distances = prep.calculate_distances(positions)
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


def check_data(pd_data):
    column_names = ['timestamp', 'position_x', 'position_y']
    return len(set(pd_data.columns) & set(column_names)) >= 3


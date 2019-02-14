import pandas as pd


class Navr:
    def __init__(self, pd_data):
        if check_data(pd_data):
            self.data = pd_data
        else:
            raise Exception('Columns not correct')
            return None


def check_data(pd_data):
    column_names = ['timestamp', 'position_x', 'position_y']
    return len(set(pd_data.columns) & set(column_names)) >= 3


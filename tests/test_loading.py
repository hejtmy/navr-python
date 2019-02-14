from navr import navr
import pandas as pd


def test_class_initialisation():
    path = 'data/bva_walking.csv'
    pd_data = pd.read_csv(path)
    n = navr.Navr(pd_data)
    assert len(n.data.columns) == 3
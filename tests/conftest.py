import pytest
import pandas as pd
from navr import navr


@pytest.fixture(scope="session")
def example_data():
    path = 'data/bva_walking.csv'
    pd_data = pd.read_csv(path)
    return pd_data


@pytest.fixture(scope="session")
def navr_class():
    pd_data = example_data()
    return navr.Navr(pd_data)

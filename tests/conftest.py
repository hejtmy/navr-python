import pytest
import pandas as pd


@pytest.fixture(scope="session")
def example_data():
    path = 'data/bva_walking.csv'
    pd_data = pd.read_csv(path)
    return pd_data

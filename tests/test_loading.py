from navr import navr
import pandas as pd
import pytest

def test_class_initialisation(example_data):
    n = navr.Navr(example_data)
    assert len(n.data.columns) == 3
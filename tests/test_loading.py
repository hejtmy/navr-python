from navr import navr


def test_class_initialisation(example_data):
    n = navr.Navr(example_data)
    assert len(n.data.columns) == 3
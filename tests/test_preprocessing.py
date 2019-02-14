# These tests actually modify the navr class
def test_distance_calculations(navr_class):
    navr_class.calculate_distances()


def test_time_calculations(navr_class):
    navr_class.calculate_time_diff()

def test_speed_calculations(navr_class):
    navr_class.calculate_speed()
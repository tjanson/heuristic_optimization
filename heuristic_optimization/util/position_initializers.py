"""Various spawn patterns within the given bounds."""
# TODO: grid, sphere

import numpy as np


def random(num_points, lower_bound, upper_bound):
    """Return random locations."""
    return np.random.uniform(low=lower_bound, high=upper_bound, size=(num_points, len(lower_bound)))

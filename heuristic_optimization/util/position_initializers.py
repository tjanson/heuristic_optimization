"""Various spawn patterns within the given bounds."""
# TODO: grid, sphere

import numpy as np


def random(num_points, lower_bound, upper_bound):
    """Return random locations."""
    return np.random.uniform(low=lower_bound, high=upper_bound, size=(num_points, len(lower_bound)))


def grid(num_points, lower_bound, upper_bound):
    dimensions = len(lower_bound)
    points_per_dimension = num_points**(1/dimensions)
    if not float(points_per_dimension).is_integer():
        raise ValueError("For grid spawns, num_points must be a power wrt # dims")
    linspaces = [np.linspace(lower_bound[i], upper_bound[i], points_per_dimension) for i in range(dimensions)]
    array_of_points = np.asarray(np.meshgrid(*linspaces)).T.reshape(-1, dimensions)
    return array_of_points

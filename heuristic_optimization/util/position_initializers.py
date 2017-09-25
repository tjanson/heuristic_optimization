"""Various spawn patterns within the given bounds."""

import numpy as np

from heuristic_optimization.util.util import clamp_into_bounds


def random(num_points, lower_bound, upper_bound):
    """Return random locations."""
    return np.random.uniform(low=lower_bound, high=upper_bound, size=(num_points, len(lower_bound)))


def grid(num_points, lower_bound, upper_bound):
    """Return (hyper-)grid of points evenly spaced in each dimension."""
    dimensions = len(lower_bound)
    points_per_dimension = num_points**(1/dimensions)
    if not float(points_per_dimension).is_integer():
        raise ValueError("For grid spawns, num_points must be a power wrt # dims")
    linspaces = [np.linspace(lower_bound[i], upper_bound[i], points_per_dimension) for i in range(dimensions)]
    array_of_points = np.asarray(np.meshgrid(*linspaces)).T.reshape(-1, dimensions)
    return array_of_points


def gaussian_distribution(number_of_points, mean_point, standard_deviation=1.0):
    """Return normal (Gaussian) distribution samples around mean point."""
    num_dimensions = len(mean_point)
    normal_samples = np.random.normal(size=(number_of_points, num_dimensions), scale=standard_deviation)
    shifted = normal_samples + mean_point
    return shifted


def clamped_gaussian_distribution(number_of_points, mean_point, bounds, standard_deviation=1.0):
    """Return Gaussian distribution clamped into bounds."""
    return clamp_into_bounds(gaussian_distribution(number_of_points, mean_point, standard_deviation), bounds)

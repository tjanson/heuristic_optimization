"""Miscellaneous helper functions that don't fit elsewhere."""

import numpy as np


def clamp_into_bounds(positions, bounds):
    """Return copy of positions clamped into bounds.

    I.e., any out-of-bounds entry is replaced by the bound.
    """
    lower_bounds, upper_bounds = bounds
    below_lower_bounds = positions < lower_bounds
    above_upper_bounds = positions > upper_bounds
    within_bounds = ~np.logical_or(below_lower_bounds, above_upper_bounds)
    bound_mask = below_lower_bounds * lower_bounds + above_upper_bounds * upper_bounds
    return np.where(within_bounds, positions, bound_mask)

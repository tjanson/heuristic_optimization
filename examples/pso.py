"""Demonstrates usage/API of the optimizer."""

from heuristic_optimization.optimizers import ParticleSwarmOptimizer


def numpy_paraboloid(arg_vector, center=0.5):
    """Generate elliptic paraboloid of arbitrary dimension."""
    return ((arg_vector - center) ** 2).sum(axis=1)


def n_dimensional_unit_bounds(num_dimensions):
    """Returns bounds of the form [0, 1]^n."""
    lower_bounds = list(0 for _ in range(num_dimensions))
    upper_bounds = list(1 for _ in range(num_dimensions))
    return lower_bounds, upper_bounds


if __name__ == '__main__':
    # the paraboloid objective function used in this demo works for an
    # arbitrary number of dimensions
    # thus the dimensionality is only determined by the search space
    # feel free to try any number of dimensions
    bounds = n_dimensional_unit_bounds(3)

    optimizer = ParticleSwarmOptimizer(numpy_paraboloid,
                                       bounds,
                                       obj_fct_is_vectorized=True,
                                       options={'num_particles': 20, 'max_iters': 25})
    optimizer.optimize()

    argmin = optimizer.historic_best_position
    minimum = optimizer.historic_best_score
    print("best arg {} yielded {}".format(argmin, minimum))

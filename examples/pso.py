"""Demonstrates usage/API of the optimizer."""

from heuristic_optimization.optimizers import ParticleSwarmOptimizer


def numpy_paraboloid(arg_vector, center=0.5):
    """Generate elliptic paraboloid of arbitrary dimension."""
    return ((arg_vector - center) ** 2).sum(axis=1)


if __name__ == '__main__':
    # the paraboloid objective function used in this demo works for an
    # arbitrary number of dimensions
    # thus the dimensionality is only determined by the search space
    # feel free to try any number of dimensions
    DIMENSIONS = 3
    LOWER_BOUNDS = list(0 for _ in range(DIMENSIONS))
    UPPER_BOUNDS = list(1 for _ in range(DIMENSIONS))
    BOUNDS = (LOWER_BOUNDS, UPPER_BOUNDS)

    optimizer = ParticleSwarmOptimizer(numpy_paraboloid,
                                       BOUNDS,
                                       obj_fct_is_vectorized=True,
                                       options={'num_particles': 20, 'max_iters': 25})
    optimizer.optimize()

    argmin = optimizer.historic_best_position
    minimum = optimizer.historic_best_score
    print("best arg {} yielded {}".format(argmin, minimum))

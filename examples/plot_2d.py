"""Visualizes batch ('population') optimizers as 2D plots."""

import numpy as np
from heuristic_optimization.optimizers import ParticleSwarmOptimizer

try:
    import matplotlib.pyplot as plt
except ImportError:
    print("This requires matplotlib (despite not being in the dependencies), but it was not found. Exiting.")
    raise


def plot(points, bounds=None):
    """Plots points in 2D (scatter plot).

    Any additional dimensions are ignored."""
    plt.scatter(points[:, 0], points[:, 1])

    if bounds is not None:
        plt.xlim(bounds[0][0], bounds[1][0])
        plt.ylim(bounds[0][1], bounds[1][1])
    plt.show()


def plot_history(history, bounds=None):
    """Plots line along historic points."""
    # shape of history: (n, m, o)
    #    n: number of particles
    #    m: dimensions of search space
    #    o: length of history
    for i in range(len(history)):
        plt.plot(history[i][0], history[i][1], 'o-')

    if bounds is not None:
        plt.xlim(bounds[0][0], bounds[1][0])
        plt.ylim(bounds[0][1], bounds[1][1])
    plt.show()


def weird_append(big_thing, slicey_thing):
    # uh, yeah, this is just meant to append along the last axis
    # not sure if there's a better way to do so. maybe relevant:
    # https://stackoverflow.com/questions/8898471/concatenate-two-numpy-arrays-in-the-4th-dimension
    return np.concatenate((big_thing, np.expand_dims(slicey_thing, -1)), -1)


if __name__ == '__main__':
    BOUNDS = ([0, 0], [1, 1])
    batch_optimizer = ParticleSwarmOptimizer(lambda A: ((A - 0.5) ** 2).sum(axis=1),
                                             BOUNDS,
                                             obj_fct_is_vectorized=True,
                                             options={'num_particles': 15, 'max_iters': 10})
    batch_optimizer.initialize()

    history = np.expand_dims(np.copy(batch_optimizer.positions), -1)
    plot_history(history, BOUNDS)

    while not batch_optimizer.stop():
        batch_optimizer.iteration += 1
        batch_optimizer.iterate()

        history = weird_append(history, batch_optimizer.positions)
        plot_history(history, BOUNDS)

    plot(batch_optimizer.positions)

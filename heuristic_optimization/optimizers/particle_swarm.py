"""
Contains particle swarm optimizer and related stuff.

For background on PSO see `Wikipedia article`_ or the original papers
by Kennedy, Eberhart and Shi.

.. _Wikipedia article:
    https://en.wikipedia.org/wiki/Particle_swarm_optimization
"""

from types import SimpleNamespace

import numpy as np

from heuristic_optimization.base import BatchOptimizer
from heuristic_optimization.util.position_initializers import random as random_positions

DEFAULT_OPTIONS = {
    'num_particles': 50,
    'max_iters': 20,
    'weight_cognition': 0.5,
    'weight_social': 0.5,
    'weight_inertia': 0.5,
}


class ParticleSwarmOptimizer(BatchOptimizer):
    """Particle swarm heuristic_optimization.

    Args:
        options: Dict of PSO-specific hyperparameters (see
            `default_options`, override values as desired).
        bounds: Tuple of size 2 where the first entry is the lower
            and the second the upper bound for objective function
            arguments (e.g., `((0,0,0), (1,1,1)`).
    """

    def __init__(self, objective_function, bounds, obj_fct_is_vectorized=False, options=None):
        # re: bounds:
        # to be honest I find this slightly unintuitive
        # an alternative format would be to group them by parameters,
        # i.e., [(0, 1, 'x'), (0, 1, 'y')]
        # I've encountered both elsewhere, both have pros and cons
        assert len(bounds) == 2 and len(bounds[0]) == len(bounds[1]), 'invalid bounds shape'

        super().__init__(objective_function, obj_fct_is_vectorized)

        self.lower_bound, self.upper_bound = np.array(bounds[0]), np.array(bounds[1])

        self.options = DEFAULT_OPTIONS.copy()
        self.options.update(options if options else {})

        self._pso_data = SimpleNamespace(velocities=None, best_positions=None, best_scores=None)

    def initialize(self):
        """Spawn particles and initialize their scores."""
        position_initializer = random_positions  # feel free to use something else
        self.positions = position_initializer(self.options['num_particles'], self.lower_bound, self.upper_bound)
        self.scores = np.array(self.compute_scores(self.positions))

        self._pso_data.best_positions = self.positions
        self._pso_data.best_scores = self.scores

        magic_constant = 2  # feel free to change FIXME
        max_velocity = self.upper_bound - self.lower_bound / magic_constant
        shape = (len(self.positions), len(self.lower_bound))
        self._pso_data.velocities = np.random.uniform(low=-max_velocity, high=max_velocity, size=shape)

    def next_positions(self):
        """Compute next positions and keep track of individual bests."""
        # FIXME triple-check all of this stuff cause I got it horribly wrong before
        self.scores = np.array(self.scores)
        improved = self.scores < self._pso_data.best_scores

        self._pso_data.best_scores[improved] = self.scores[improved]
        self._pso_data.best_positions[improved] = self.positions[improved]

        self._pso_data.velocities = self._new_velocities()
        new_positions = self.positions + self._pso_data.velocities
        return new_positions

    def stop(self):
        """Return True when max_iters is reached."""
        return not self.iteration < self.options['max_iters']

    def _new_velocities(self):
        """Compute velocities based on three factors as defined in PSO."""
        opts = self.options
        # has shape (100, 1), as opposed to (100,) for multiplication with (100, 2)
        rand1, rand2 = [np.random.rand(len(self._pso_data.velocities))[:, None] for _ in range(2)]

        current_best_position = self.positions[np.argmin(self.scores)]

        inertia = opts['weight_inertia'] * self._pso_data.velocities
        cognition = opts['weight_cognition'] * rand1 * (self._pso_data.best_positions - self.positions)
        social = opts['weight_social'] * rand2 * (current_best_position - self.positions)

        new_velocities = inertia + cognition + social
        preliminary_positions = self.positions + new_velocities
        new_positions = self._clamp_into_bounds(preliminary_positions)

        return new_positions - self.positions

    def _clamp_into_bounds(self, positions):
        """Return copy of positions clamped into bounds.

        I.e., any out-of-bounds entry is replaced by the bound.
        """
        below_lower_bounds = positions < self.lower_bound
        above_upper_bounds = positions > self.upper_bound
        within_bounds = ~np.logical_or(below_lower_bounds, above_upper_bounds)
        bound_mask = below_lower_bounds * self.lower_bound + above_upper_bounds * self.upper_bound
        return np.where(within_bounds, positions, bound_mask)

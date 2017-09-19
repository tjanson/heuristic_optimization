"""Contains base class for iterative optimization procedures."""

from heuristic_optimization.base import Optimizer


class IterativeOptimizer(Optimizer):
    """Base class for iterative heuristic_optimization procedures."""

    def __init__(self, objective_function, obj_fct_is_vectorized=False):
        super().__init__(objective_function, obj_fct_is_vectorized)
        self.iteration = 0

    def optimize(self):  # noqa: D401
        """Iteratively optimize."""
        self.initialize()

        while not self.stop():
            self.iteration += 1
            self.iterate()

    def initialize(self):
        """Do what is necessary before the first iteration."""
        raise NotImplementedError

    def iterate(self):
        """Perform a single heuristic_optimization iteration."""
        raise NotImplementedError

    def stop(self):
        """Return True if the optimizer should stop now.

        Called before every iteration. The entire procedure will run
        while this is still True.
        """
        raise NotImplementedError

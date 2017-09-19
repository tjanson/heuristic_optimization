"""Contains base class for iterative batch optimization procedures."""

from heuristic_optimization.base import IterativeOptimizer


# It's possible that this is sort of unnecessary, as in: every
# IterativeOptimizer is a (possibly trivial) BatchOptimizer.
# But I think this is somewhat convenient and mostly it'll help me get
# closer to the sampling (in mindset at least).
class BatchOptimizer(IterativeOptimizer):
    """Base class for iterative, batch-evaluation optimizers.

    Such optimizers generate a set of positions in each iteration,
    which is then evaluated. The next batch is determined based on
    these results.
    """

    def __init__(self, objective_function, obj_fct_is_vectorized=False):
        super().__init__(objective_function, obj_fct_is_vectorized)
        self.positions = None
        self.scores = None

    def iterate(self):
        """Update positions and scores."""
        self.positions = self.next_positions()
        self.scores = self.compute_scores(self.positions)
        self._update_historic_best(self.positions, self.scores)

    def next_positions(self):
        """Return next batch of positions to be evaluated."""
        raise NotImplementedError

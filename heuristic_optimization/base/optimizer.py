"""Contains optimizer base class."""


def _vectorize(fct):  # noqa: D202
    """Vectorize function so that it operates on and returns a list."""
    # TODO: parallelize this with multiprocessing (but make that configurable)
    # also, this (entire concept) doesn't exactly seem pretty
    # principle of least astonishment and whatnot

    def vectorized_function(list_of_args):  # pylint: disable=missing-docstring
        return [fct(arg) for arg in list_of_args]

    vectorized_function.__doc__ = fct.__doc__
    return vectorized_function


class Optimizer:
    """Base class for mathematical heuristic_optimization procedures.

    We always use a vectorized objective function, i.e., function
    evaluation is performed in batches. For some functions, this can
    enable better performance.

    Args:
        objective_function: Function to be minimized.
        obj_fct_is_vectorized: Boolean indicating whether the objective
            function is already vectorized.
    """

    def __init__(self, objective_function, obj_fct_is_vectorized=False):
        if not obj_fct_is_vectorized:
            objective_function = _vectorize(objective_function)
        self._vectorized_objective_function = objective_function

        self.historic_best_score = None
        self.historic_best_position = None

    def optimize(self):
        """Return argmin and min of the objective function."""
        raise NotImplementedError

    def compute_scores(self, positions):
        """Evaluate objective function at given positions.

        Args:
            positions: Iterable of arguments for the objective
                function.
        """
        scores = self._vectorized_objective_function(positions)
        self._update_historic_best(positions, scores)
        return scores

    def _update_historic_best(self, positions, scores):
        best_index, best_score = min(enumerate(scores), key=lambda x: x[1])
        if self.historic_best_score is None or best_score < self.historic_best_score:
            self.historic_best_score = best_score
            self.historic_best_position = positions[best_index]

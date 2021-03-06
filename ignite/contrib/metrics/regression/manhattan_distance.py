import torch

from ignite.contrib.metrics.regression._base import _BaseRegression


class ManhattanDistance(_BaseRegression):
    r"""
    Calculates the Manhattan Distance:

    :math:`\text{MD} = \sum_{j=1}^n (A_j - P_j)`,

    where :math:`A_j` is the ground truth and :math:`P_j` is the predicted value.

    More details can be found in `Botchkarev 2018`__.

    - ``update`` must receive output of the form ``(y_pred, y)`` or ``{'y_pred': y_pred, 'y': y}``.
    - `y` and `y_pred` must be of same shape `(N, )` or `(N, 1)`.

    __ https://arxiv.org/abs/1809.03006

    """

    def reset(self):
        self._sum_of_errors = 0.0

    def _update(self, output):
        y_pred, y = output
        errors = y.view_as(y_pred) - y_pred
        self._sum_of_errors += torch.sum(errors).item()

    def compute(self):
        return self._sum_of_errors

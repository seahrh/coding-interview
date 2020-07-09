import math
import random
from typing import List, Union, Callable
from geometry.linear_algebra import dot

Numeric = Union[int, float]


def relu(value: Numeric) -> float:
    return max(0, value)


def he_normal(fan_in: int) -> float:
    return random.gauss(0, 1) * math.sqrt(2 / fan_in)


class HiddenUnit:
    def __init__(
        self,
        n_weights: int,
        activation: Callable[[Numeric], float],
        initialization: Callable[[int], float],
    ):
        # weights shape (#weights, 1)
        self.weights: List[List[float]] = [[initialization(n_weights)]] * n_weights
        self.bias: float = initialization(n_weights)
        self._activation = activation

    def eval(self, xs: List[List[float]]) -> List[float]:
        """Returns a list of activation values (one per example).

        :param xs: Input data shape (#examples, #features)
        :return:
        """
        if len(self.weights) != len(xs[0]):
            raise ValueError("Number of weights must equal the number of features")
        xw: List[List[float]] = dot(xs, self.weights)
        res: List[float] = []
        for i in range(len(xw)):
            z = self._activation(xw[i][0] + self.bias)
            res.append(z)
        return res


class DenseNet:
    def __init__(
        self,
        input_layer_size: int,
        hidden_layer_size: List[int],
        output_layer_size: int,
        activation: Callable[[Numeric], float] = relu,
        initialization: Callable[[int], float] = he_normal,
    ):
        self._input_layer_size = input_layer_size
        self._hidden_layer_size = hidden_layer_size
        self._output_layer_size = output_layer_size
        self._activation = activation
        self._initialization = initialization

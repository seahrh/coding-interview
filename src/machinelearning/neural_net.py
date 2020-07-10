import math
import random
from abc import ABC, abstractmethod
from typing import List, Union, Callable, Type

from geometry.linear_algebra import dot, transpose

Numeric = Union[int, float]


class Activation(ABC):
    @staticmethod
    @abstractmethod
    def apply(x: Numeric) -> float:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def derivative(x: Numeric) -> float:
        raise NotImplementedError


class ReluActivation(Activation):
    @staticmethod
    def apply(x: Numeric) -> float:
        return max(0, x)

    @staticmethod
    def derivative(x: Numeric) -> float:
        if x > 0:
            return 1
        # When x == 0, derivative does not exist. So use arbitrary value of zero.
        # When x < 0, flat gradient so derivative == 0
        return 0


def he_normal(fan_in: int) -> float:
    return random.gauss(0, 1) * math.sqrt(2 / fan_in)


class Neuron:
    """
    A neuron in a hidden layer is also known as a hidden unit.
    """

    def __init__(
        self,
        n_weights: int,
        activation: Type[Activation],  # accepts any subclass
        initialization: Callable[[int], float],
    ):
        # weights shape (#weights, 1)
        self.weights: List[List[float]] = [[initialization(n_weights)]] * n_weights
        self.bias: float = initialization(n_weights)
        self._activation = activation

    def forward_propagate(self, xs: List[List[float]]) -> List[float]:
        """Returns a list of activation values (one per example).

        :param xs: Input data shape (#examples, #features)
        :return:
        """
        if len(self.weights) != len(xs[0]):
            raise ValueError("Number of weights must equal the number of features")
        xw: List[List[float]] = dot(xs, self.weights)
        res: List[float] = []
        for i in range(len(xw)):
            z = self._activation.apply(xw[i][0] + self.bias)
            res.append(z)
        return res


class DenseNet:
    """
    In a dense net, all layers are fully connected.
    """

    def __init__(
        self,
        hidden_layer_sizes: List[int],
        output_layer_size: int,
        activation: Type[Activation] = ReluActivation,  # accepts any subclass
        initialization: Callable[[int], float] = he_normal,
    ):
        self._n_hidden_layers = len(hidden_layer_sizes)
        self._hidden_layer_sizes = hidden_layer_sizes
        self._output_layer_size = output_layer_size
        self._layers: List[List[Neuron]] = []
        self._activation = activation
        self._initialization = initialization

    def _init_params(self, n_weights: int) -> None:
        for i in range(self._n_hidden_layers):
            neurons = [
                Neuron(
                    n_weights,
                    activation=self._activation,
                    initialization=self._initialization,
                )
                for _ in range(self._hidden_layer_sizes[i])
            ]
            self._layers.append(neurons)
        output_layer = [
            Neuron(
                n_weights,
                activation=self._activation,
                initialization=self._initialization,
            )
            for _ in range(self._output_layer_size)
        ]
        self._layers.append(output_layer)

    def _forward_propagate(self, data: List[List[Numeric]]):
        xs: List[List[Numeric]] = data
        for layer in self._layers:
            zs: List[List[float]] = []
            for neuron in layer:
                z = neuron.forward_propagate(xs)
                zs.append(z)
            xs = transpose(zs)

    def fit(self, data: List[List[Numeric]], epochs: int = 1) -> None:
        n_features = len(data[0])
        self._init_params(n_features)
        for epoch in range(epochs):
            self._forward_propagate(data)

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


class Relu(Activation):
    @staticmethod
    def apply(z: Numeric) -> float:
        """Applies the rectified linear unit activation function.

        :param z: WX the weighted input
        :return: activation value
        """
        return max(0, z)

    @staticmethod
    def derivative(z: Numeric) -> float:
        """Returns the derivative of the activation function with respect to Z.

        :param z: WX the weighted input
        :return: partial derivative of activation function with respect to Z.
        """
        if z > 0:
            return 1
        # When x == 0, derivative does not exist. So use arbitrary value of zero.
        # When x < 0, flat gradient so derivative == 0
        return 0


class Cost(ABC):
    @staticmethod
    @abstractmethod
    def apply(y: Numeric, yhat: Numeric) -> float:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def derivative(y: Numeric, yhat: Numeric) -> float:
        raise NotImplementedError


class SimpleCost(Cost):
    @staticmethod
    def apply(y: Numeric, yhat: Numeric) -> float:
        return 0.5 * (yhat - y) ** 2

    @staticmethod
    def derivative(y: Numeric, yhat: Numeric) -> float:
        return yhat - y


def he_normal(fan_in: int) -> float:
    """He Normal initialization"""
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
            a = self._activation.apply(xw[i][0] + self.bias)
            res.append(a)
        return res


class DenseNet:
    """
    In a dense net, all layers are fully connected.
    """

    def __init__(
        self,
        hidden_layer_sizes: List[int],
        output_layer_size: int,
        cost: Type[Cost] = SimpleCost,
        activation: Type[Activation] = Relu,  # accepts any subclass
        initialization: Callable[[int], float] = he_normal,
    ):
        self._n_hidden_layers = len(hidden_layer_sizes)
        self._hidden_layer_sizes = hidden_layer_sizes
        self._output_layer_size = output_layer_size
        self._layers: List[List[Neuron]] = []
        self._cost = cost
        # Cost history has the shape (#epochs, #targets, #examples)
        self.costs: List[List[List[float]]] = []
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

    def _forward_propagate(self, X: List[List[Numeric]]) -> List[List[float]]:
        # training data shape (#examples, #features or #neurons)
        inp: List[List[float]] = X
        # activations shape (#neurons, #examples)
        activations: List[List[float]] = []
        for layer in self._layers:
            activations = []
            for neuron in layer:
                a = neuron.forward_propagate(inp)
                activations.append(a)
            inp = transpose(activations)
        return activations

    def fit(self, X: List[List[Numeric]], y: List[Numeric], epochs: int = 1) -> None:
        n_features = len(X[0])
        self._init_params(n_features)
        self.costs = []
        for epoch in range(epochs):
            targets = self._forward_propagate(X)
            target_costs: List[List[float]] = []
            for target in targets:
                costs: List[float] = []
                for i in range(len(y)):
                    c = self._cost.apply(y[i], yhat=target[i])
                    costs.append(c)
                target_costs.append(costs)
            self.costs.append(target_costs)

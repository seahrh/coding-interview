import math
import random
from abc import ABC, abstractmethod
from typing import List, Union, Callable, Type

from geometry.linear_algebra import dot, transpose, full

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
        # When z == 0, derivative does not exist. So use arbitrary value of zero.
        # When z < 0, flat gradient so derivative == 0
        return 0


class Cost(ABC):
    """Cost function for a single example, allows for multiple targets."""

    @staticmethod
    @abstractmethod
    def apply(y: List[Numeric], y_hat: List[Numeric]) -> float:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def derivative(y: List[Numeric], y_hat: List[Numeric]) -> float:
        raise NotImplementedError


class SquaredError(Cost):
    @staticmethod
    def apply(y: List[Numeric], y_hat: List[Numeric]) -> float:
        _sum: float = 0
        for i in range(len(y)):
            _sum += (y_hat[i] - y[i]) ** 2
        return 0.5 * _sum

    @staticmethod
    def derivative(y: List[Numeric], y_hat: List[Numeric]) -> float:
        _sum: float = 0
        for i in range(len(y)):
            _sum += math.fabs(y_hat[i] - y[i])
        return _sum


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
        self.weights: List[List[float]] = [
            [initialization(n_weights)] for _ in range(n_weights)
        ]
        self.bias: float = initialization(n_weights)
        self._activation = activation
        # output of linear function before activation
        self.zs: List[float] = []

    def forward_propagate(self, batch: List[List[float]]) -> List[float]:
        """Returns a list of activation values (one per example).

        :param batch: Input data shape (#examples, #features)
        :return:
        """
        if len(self.weights) != len(batch[0]):
            raise ValueError("Number of weights must equal the number of features")
        xw: List[List[float]] = dot(batch, self.weights)
        self.zs = []
        res: List[float] = []
        for i in range(len(xw)):
            z = xw[i][0] + self.bias
            self.zs.append(z)
            a = self._activation.apply(z)
            res.append(a)
        return res

    def backward_propagate(
        self, batch: List[List[float]], error_terms: List[float], learning_rate: float,
    ) -> None:
        if len(self.zs) != len(batch):
            raise ValueError(
                "Length of output must equal the number of training examples"
            )
        if len(self.zs) != len(error_terms):
            raise ValueError(
                "Length of output must equal the number of cost derivatives"
            )
        gradients: List[float] = [0] * len(self.weights)
        for i in range(len(self.zs)):
            dc_da = error_terms[i]
            da_dz = self._activation.derivative(self.zs[i])
            for j in range(len(self.weights)):
                dz_dw = batch[i][j]
                # Chain rule, average gradients for the batch
                gradients[j] += dc_da * da_dz * dz_dw / len(batch)
        for i in range(len(gradients)):
            self.weights[i][0] -= learning_rate * gradients[i]

    def gradient_wrt_input(self) -> List[List[float]]:
        """Returns the output derivative wrt. input.

        :return: gradients shape (#examples, #weights)
        """
        # activation gradients (#examples, 1)
        da_dz: List[List[float]] = []
        for z in self.zs:
            da_dz.append([self._activation.derivative(z)])
        return dot(da_dz, transpose(self.weights))


class DenseNet:
    """
    In a dense net, all layers are fully connected.
    """

    def __init__(
        self,
        hidden_layer_sizes: List[int],
        output_layer_size: int,
        cost: Type[Cost] = SquaredError,
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

    def _forward_propagate(self, batch: List[List[Numeric]]) -> List[List[float]]:
        """One forward pass per batch.

        :param batch: batch (#examples, #features)
        :return: output from output layer (#examples, #targets)
        """
        inp: List[List[float]] = batch
        for layer in self._layers:
            # layer output (#neurons or #targets, #examples)
            out: List[List[float]] = []
            for neuron in layer:
                a: List[float] = neuron.forward_propagate(inp)
                out.append(a)
            inp = transpose(out)
        return inp

    def _backward_propagate(
        self,
        batch: List[List[Numeric]],
        y: List[List[Numeric]],
        output: List[List[Numeric]],
        learning_rate: float,
    ) -> None:
        batch_size = len(batch)
        # error_terms (#neurons in layer, batch size)
        error_terms: List[List[float]] = [[] for _ in range(self._output_layer_size)]
        for i in range(batch_size):  # for each example
            c = self._cost.derivative(y[i], y_hat=output[i])
            for j in range(self._output_layer_size):
                error_terms[j].append(c)
        for i in range(len(self._layers) - 1, -1, -1):
            layer = self._layers[i]
            downstream_layer_size = len(self._layers[i - 1]) if i != 0 else 1
            tmp: List[List[float]] = full(
                rows=downstream_layer_size, columns=batch_size, fill=0
            )
            for j in range(len(layer)):
                neuron = layer[j]
                neuron.backward_propagate(
                    batch, error_terms=error_terms[j], learning_rate=learning_rate,
                )
                # no need to update error terms in the first hidden layer
                if i == 0:
                    continue
                # gradients wrt input (#weights, batch size)
                gradients = transpose(neuron.gradient_wrt_input())
                n_weights = len(gradients)
                for w in range(n_weights):
                    for k in range(batch_size):
                        tmp[w][k] = gradients[w][k] * error_terms[j][k]
            error_terms = tmp

    def _iteration(
        self, batch: List[List[Numeric]], y: List[List[Numeric]], learning_rate: float,
    ) -> None:
        """Run one iteration on one batch."""
        output = self._forward_propagate(batch)
        self._backward_propagate(batch, y, output, learning_rate)

    def fit(
        self,
        X: List[List[Numeric]],
        y: List[List[Numeric]],
        learning_rate: float = 0.1,
        batch_size: int = 1,
        epochs: int = 1,
    ) -> None:
        n_features = len(X[0])
        self._init_params(n_features)
        self.costs = []
        for epoch in range(epochs):
            i = 0
            while i + batch_size < len(X):
                batch = X[i : i + batch_size]
                self._iteration(batch, y, learning_rate)
                i += batch_size
            if i < len(X):
                batch = X[i:]
                self._iteration(batch, y, learning_rate)

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
    @staticmethod
    @abstractmethod
    def apply(y: Numeric, y_hat: Numeric) -> float:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def derivative(y: Numeric, y_hat: Numeric) -> float:
        raise NotImplementedError


class SimpleCost(Cost):
    @staticmethod
    def apply(y: Numeric, y_hat: Numeric) -> float:
        return 0.5 * (y_hat - y) ** 2

    @staticmethod
    def derivative(y: Numeric, y_hat: Numeric) -> float:
        return y_hat - y


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
        self,
        batch: List[List[float]],
        upstream_gradients: List[float],
        learning_rate: float,
    ) -> None:
        if len(self.zs) != len(batch):
            raise ValueError(
                "Length of output must equal the number of training examples"
            )
        if len(self.zs) != len(upstream_gradients):
            raise ValueError(
                "Length of output must equal the number of cost derivatives"
            )
        gradients: List[float] = [0] * len(self.weights)
        for i in range(len(self.zs)):
            dc_da = upstream_gradients[i]
            da_dz = self._activation.derivative(self.zs[i])
            for j in range(len(self.weights)):
                dz_dw = batch[i][j]
                # Chain rule, average gradients for the batch
                gradients[j] += dc_da * da_dz * dz_dw / len(batch)
        for i in range(len(gradients)):
            self.weights[i][0] -= learning_rate * gradients[i]

    def gradient_wrt_input(self) -> List[List[float]]:
        """Returns the output derivative wrt. input.

        :return: gradients shape (#weights, #examples)
        """
        # activation values in matrix form (1, #examples)
        z_matrix: List[List[float]] = [self.zs]
        return dot(self.weights, z_matrix)


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
        # upstream gradients (#neurons, #examples)
        upstream_gradients: List[List[float]] = []
        for i in range(len(y[0])):  # for each target variable
            cost_gradients = []
            for j in range(batch_size):  # for each example
                c = self._cost.derivative(y[j][i], y_hat=output[j][i])
                cost_gradients.append(c)
            upstream_gradients.append(cost_gradients)
        for i in range(len(self._layers) - 1, -1, -1):
            layer = self._layers[i]
            downstream_layer_size = len(layer[0].weights)
            tmp: List[List[float]] = full(
                rows=downstream_layer_size, columns=batch_size, fill=0
            )
            for j in range(len(layer)):
                neuron = layer[j]
                neuron.backward_propagate(
                    batch,
                    upstream_gradients=upstream_gradients[j],
                    learning_rate=learning_rate,
                )
                gradients = neuron.gradient_wrt_input()
                for w in range(len(tmp)):  # for each weight
                    for ex in range(len(tmp[0])):  # for each example
                        # take simple average
                        tmp[w][ex] += (
                            upstream_gradients[j][ex]
                            * gradients[w][ex]
                            / downstream_layer_size
                        )
            upstream_gradients = tmp

    def _update(self, batch: List[List[Numeric]], y: List[List[Numeric]]) -> None:
        # output shape (#targets, #examples)
        out = self._forward_propagate(batch)
        costs: List[List[float]] = [[]]
        for i in range(len(out)):
            for j in range(len(out[0])):
                pass

    def fit(
        self,
        X: List[List[Numeric]],
        y: List[List[Numeric]],
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
                i += batch_size
                pass

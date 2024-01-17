"""
Linear regression with SGD
Based on https://medium.com/@nikhilparmar9/simple-sgd-implementation-in-python-for-linear-regression-on-boston-housing-data-f63fcaaecfb1
"""
import numpy as np


def my_sgd(X, y, learning_rate, n_iter):
    """Linear regression with SGD

    :param X: One minibatch of shape (#examples, #features)
    :param y: ground truth of shape (#examples, 1)
    :param learning_rate:
    :param n_iter: Stop learning when number of iterations is reached
    :return:
    """
    w = np.zeros(shape=(1, X.shape[1]))
    b = 0
    while n_iter > 0:
        # reset gradients after weight update
        w_gradient = np.zeros(shape=(1, X.shape[1]))
        b_gradient = 0
        for i in range(len(X)):
            # y_pred = np.dot(w, X[i]) + b
            # loss = (y[i] - y_pred) ** 2
            # derivative of L wrt W
            w_gradient += (-2 * X[i] ** 2) - (2 * X[i] * y[i]) + (2 * b * X[i])
            # derivative of L wrt b
            b_gradient += (2 * b) - (2 * y[i]) + (2 * w * X[i])
        w -= learning_rate * (w_gradient / len(X))
        b -= learning_rate * (b_gradient / len(X))
        n_iter -= 1
    return w, b

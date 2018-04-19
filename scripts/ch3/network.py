import numpy as np
from sigmoid import sigmoid


def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['B1'] = np.array([0.1, 0.2, 0.3])
    network['B2'] = np.array([0.1, 0.2])
    network['B3'] = np.array([0.1, 0.2])

    return network


def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    B1, B2, B3 = network['B1'], network['B2'], network['B3']
    A1 = np.dot(x, W1) + B1
    print(A1)
    z1 = sigmoid(A1)

    A2 = np.dot(z1, W2) + B2
    z2 = sigmoid(A2)
    print(A2)

    y = np.dot(z2, W3) + B3

    return y


if __name__ == '__main__':
    print ('forward network')
    x = np.array([1.0, 0.5])
    network = init_network()
    y = forward(network, x)

    print(y)

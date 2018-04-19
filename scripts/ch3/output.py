import numpy as np

def softmax(x):
    C = np.max(x)

    exp = np.exp(x - C)
    sum_exp = np.sum(exp)

    return exp / sum_exp


if __name__ == '__main__':
    x = np.array([1010, 1000, 990])

    y = softmax(x)

    print(y)
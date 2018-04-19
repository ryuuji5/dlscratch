import numpy as np

def relu(x):
    """
    if x <= 0:
        return 0
    elif x > 0:
        return x
    """
    return np.maximum(0, x)

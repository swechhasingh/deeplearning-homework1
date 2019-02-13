import numpy as np


class Relu:

    def __init__(self):
        pass

    def relu(self, input):
        return np.maximum(input, 0.)

    def derivative(self, input):
        input[input > 0.] = 1.
        return input

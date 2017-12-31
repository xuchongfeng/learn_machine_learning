#!/usr/bin/python
# coding: utf-8

import numpy as np

DATA_PATH = r"C:\Users\Administrator\PycharmProjects\learn_machine_learning\perceptron\dataset\data.dat"


def init():
    data = np.loadtxt(DATA_PATH)
    X = data[:,0:-1]
    y = data[:,-1]
    return X, y


class Perceptron(object):
    def __init__(self, w_shape, learning_rate=0.01):
        self.w = np.random.rand(w_shape[1], w_shape[0])
        self.b = np.random.rand(1)
        self.learning_rate = learning_rate

    def fit(self, X, y):
        while True:
            w, b = np.copy(self.w), np.copy(self.b)
            count = 0
            for i in range(len(X)):
                if y[i] * ((np.dot(w, X[i])) + b) < 0:
                    count += 1
                    self.w += self.learning_rate * y[i] * X[i]
                    self.b += self.learning_rate * y[i]
            if count == 0: break

    def predict(self, x):
        return 1 if self.w * x + self.b > 0 else -1


def main():
    X, y = init()
    perceptron = Perceptron((X.shape[1], 1))
    perceptron.fit(X, y)
    print(perceptron.w, perceptron.b)

if __name__ == "__main__":
    main()


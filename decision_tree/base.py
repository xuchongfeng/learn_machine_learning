#!/usr/bin/python
# coding: utf-8

import numpy as np


class Base(object):
    def __init__(self, depth, epsilon):
        self.depth = depth
        self.epsilon = epsilon

    def fit(self):
        pass

    def predict(self):
        pass

    def build(self, X, y):
        return self.build_helper(X, y, 0)

    def build_helper(self, X, y, depth):
        if depth > self.depth or self.limit() < self.epsilon:
            value = np.argmax(np.bincount(y))
            return TreeNode(None, None, X, y, value)

        X1, y1, X2, y2 = self.split(X, y)
        left = self.build_helper(X1, y1, depth+1)
        right = self.build_helper(X2, y2, depth+1)
        return TreeNode(left, right, X, y, None)

    def entropy(self, X, y):
        total_count = y.shape[0]
        value, cnt = np.unique(y, return_counts=True)
        cnt = cnt + 0.0
        p = cnt / total_count
        entropy = -np.sum(p * np.log2(p))
        return entropy

    def entropy_gain(self, X, y):
        sample_num, feature_num = X.shape[0], X.shape[1]
        hd = self.entropy(X, y)
        data = np.concatenate((X, y), axis=1)


    def limit(self):
        pass

    def split(self):
        pass


class Tree(object):
    def __init__(self, root):
        self.root = root


class TreeNode(object):
    def __init__(self, left, right, X, y, value):
        self.left = left
        self.right = right
        self.X = X
        self.y = y
        self.value = value


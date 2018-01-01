#!/usr/bin/python
# coding: utf-8

import numpy as np


class KDNode(object):
    def __init__(self, X, y, left, right):
        self.X = X
        self.y = y
        self.left = left
        self.right = right


class KDTree(object):
    def __init__(self, X, y):
        self.X = X
        self.y = y
        self.root = None

    def build(self):
        return self._build_helper(self.X, self.y, 0)

    def _build_helper(self, X, y, level):
        index = level % X.shape(1) + 1


def main():
    pass

if __name__ == "__main__":
    pass

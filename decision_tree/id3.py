#!/usr/bin/python
# coding: utf-8

from .base import Base


class ID3(Base):
    def __init__(self, depth, epsilon):
        super(ID3, self).__init__(depth, epsilon)

    def limit(self, X, y):
        pass

    def split(self, X, y):
        max_entropy_gain = 0
        feature_index, feature_value = 0, 0
        data_num, feature_num = X.shape[0], X.shape[1]


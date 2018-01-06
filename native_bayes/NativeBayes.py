#!/usr/bin/python
# coding: utf-8

from os import listdir
from os.path import isfile, join


class NativeBayes(object):
    def __init__(self):
        pass

    def fit(self, X, y):
        pass

    def predict(self, X):
        pass


def get_word_vector(file_path):
    words = set()
    for file in listdir(file_path):
        if isfile(join(file_path, file)):
            f = open(file)
            for line in f.readlines():
                word = line.split("")
                words.add(word)
    return words


def file_word_count(file):
    file_words = {}
    for line in file.readlines():
        for word in line.split(""):
            count = file_words.get(word, 0)
            file_words[word] = count + 1
    return file_words



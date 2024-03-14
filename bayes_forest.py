import numpy as np
from collections import defaultdict
import os
import csv
from random import shuffle
from typing import (NamedTuple)
from sklearn.preprocessing import OneHotEncoder

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.ensemble import BaggingClassifier

#-------------------Data preparation-------------------
def displayText():
    print( "hello test")
class Data(NamedTuple):
    sample_class: str
    values: list
def read_data(filename, class_column=6):
    filepath = os.path.join(os.getcwd(), filename)
    data = []
    with open(filepath, mode="r", newline="") as file:
        for line in csv.reader(file):
            class_label = line[class_column]
            attributes = line[:class_column] + line[class_column+1:] # remove class label
            sample = Data(class_label, attributes)
            data.append(sample)
    return data
def split_data(data):
    shuffle(data)   #here i want to avoid over-fitting
    train_size = 8 * len(data) // 10
    train_data = data[:train_size]
    test_data = data[train_size:]
    return train_data, test_data
def encoding(data):
    X = []
    y = []

    for i in range(len(data)):
        X.append(data[i].values)
        y.append(data[i].sample_class)

    X_arr = np.array(X)
    y_arr = np.array(y)

    X_encoded = OneHotEncoder().fit_transform(X_arr).toarray()
    y_encoded = y_arr.reshape(-1)

    return X_encoded, y_encoded

#-------------------Naive Bayes-------------------
class NaiveBayes:
    def __init__(self):
        self.prior = None  # a'priori likelihood
        self.likelihood = None  # conditional likelihood
    def fit(self, X, y, smoothing=1):
        self.prior = defaultdict(int)
        self.likelihood = {}

        for label in y:
            self.prior[label] += 1  # the number of occurrences of each class

        for label in np.unique(y):  # conditional likelihood for individual characteristics
            indices = np.where(y == label)[0]
            self.likelihood[label] = (X[indices].sum(axis=0) + smoothing) / (len(indices) + 2 * smoothing)
    def predict(self, X):
        if self.prior is None or self.likelihood is None:
            raise ValueError("Error. You cannot predict class without training")
        posteriors = []
        for x in X:
            posterior = self.prior.copy()
            for label, likelihood_label in self.likelihood.items():
                for i, bool_value in enumerate(x):
                    posterior[label] *= likelihood_label[i] if bool_value else (
                            1 - likelihood_label[i])
            sum_posterior = sum(posterior.values())
            for label in posterior:
                if posterior[label] == float('inf'):
                    posterior[label] = 1.0
                else:
                    posterior[label] /= sum_posterior
            posteriors.append(posterior.copy())
        return np.array([max(prediction, key=prediction.get)
                         for prediction in posteriors])
def compare_Bayes(X_train, y_train, X_test, y_test):
    clf = GaussianNB()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy

#-------------------Random Forest-------------------
class RandomForest:
    def __init__(self, n_estimators, classifier):
        self.clf = classifier
        self.n_estimators = n_estimators
    def bagging(self, X, y):
        samples_lines = np.random.choice(a=X.shape[0], size=X.shape[0], replace=True)
        return X[samples_lines], y[samples_lines]
    def fit(self, X, y):
        clfs = []
        for i in range(self.n_estimators):
            clf = self.clf()
            X_sample, y_sample = self.bagging(X, y) #bootstrap aggregation
            clf.fit(X_sample, y_sample)
            clfs.append(clf)
        self.classifiers = clfs
        return self.classifiers
    def predict(self, X):
        if self.classifiers is None:
            raise ValueError("Error. You cannot predict class without training")
        predicted = np.array([clf.predict(X) for clf in self.classifiers])
        result = []
        for i in range(predicted.shape[1]):
            unique, counts = np.unique(predicted[:, i], return_counts=True)
            result.append(unique[np.argmax(counts)])

        return np.array(result)
def compare_RandomForest(X_train, y_train, X_test, y_test, smoothing, n):
    naive_bayes = GaussianNB(var_smoothing=smoothing)
    random_forest = BaggingClassifier(estimator=naive_bayes, n_estimators=n)
    random_forest.fit(X_train, y_train)
    y_pred = random_forest.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy
from django.shortcuts import render
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def supervisedlearning_view(request, *args, **kwargs):
    my_context = {"my_methods": ["Nearest Neighbors",
                                 "Linear SVM",
                                 "RBF SVM",
                                 "Gaussian Process",
                                 "Decision Tree",
                                 "Random Forest",
                                 "Neural Net",
                                 "AdaBoost",
                                 "Naive Bayes",
                                 "QDA"]}

    return render(request, "homeSL.html", my_context)

def knn_view(request, *args, **kwargs):
    my_context = {"my_methods": ["Nearest Neighbors"]}
    X, y = make_blobs(n_samples=800, n_features=2, centers=9, cluster_std=1.5, random_state=4)
    plt.style.use('seaborn')
    plt.figure(figsize=(10, 10))
    plt.scatter(X[:, 0], X[:, 1], c=y, marker='*', s=100, edgecolors='black')
    plt.show()

    return render(request, "knn.html", my_context)



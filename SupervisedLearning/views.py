from django.shortcuts import render
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.cm as cm
import sys
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

    x = [6, 7, 11, 6, 4, 12, 15, 9, 11, 13]
    y = [22, 29, 23, 17, 18, 26, 25, 23, 22, 23]
    classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]

    plt.scatter(x , y , c=classes )

    plt.show()


    data = list(zip(x, y))
    knn = KNeighborsClassifier(n_neighbors=5)

    knn.fit(data, classes)

    new_x = 8
    new_y = 21
    new_point = [(new_x, new_y)]

    prediction = knn.predict(new_point)

    plt.scatter(x + [new_x], y + [new_y], c=classes + [prediction[0]])
    plt.text(x=new_x - 1.7, y=new_y - 0.7, s=f"new point, class: {prediction[0]}")
    plt.show()

    # Two  lines to make our compiler able to draw:
    plt.savefig("d://abc.jpg")


    return render(request, "knn.html", my_context)



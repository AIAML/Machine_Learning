from django.shortcuts import render

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




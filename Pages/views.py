from django.shortcuts import render
from django.http import HttpResponse

def home_view(request,*args,**kwargs):
    #my_context = {"my_text":"This is main page","my_number":134}
    return render(request,"home.html", {})

def supervisedlearning_view(request,*args,**kwargs):
    my_context = {"my_methods":["Nearest Neighbors",
    "Linear SVM",
    "RBF SVM",
    "Gaussian Process",
    "Decision Tree",
    "Random Forest",
    "Neural Net",
    "AdaBoost",
    "Naive Bayes",
    "QDA"]}

    return render(request,"supervisedlearning.html", my_context)

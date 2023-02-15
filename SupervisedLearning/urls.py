from SupervisedLearning.views import supervisedlearning_view,knn_view
from django.urls import include, path,include
urlpatterns = [
path('', supervisedlearning_view, ''),
path('knn/', knn_view, ''),]

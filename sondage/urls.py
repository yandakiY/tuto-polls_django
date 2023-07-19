from django.urls import path
from . import views

app_name = "sondage"
urlpatterns = [
    path('' , views.IndexView.as_view() , name="index"),
    path('<int:pk>' , views.QuestionDetailView.as_view() , name="details"),
    path('<int:pk>/results' , views.ResultView.as_view() , name="results")
]

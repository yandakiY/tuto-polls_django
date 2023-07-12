from django.urls import path
from . import views
# Link to my index function in views.py

app_name = 'polls'

urlpatterns = [
    # ex : /polls
    path("", views.IndexView.as_view(), name="index"),
    
    #ex : details : /polls/3
    path("<int:pk>/" , views.DetailView.as_view() , name="details"),
    
    # ex results : /polls/3/results
    path("<int:pk>/results", views.ResultsView.as_view() , name="results"),
    
    # votes : /polls/3/votes
    path("<int:question_id>/votes" , views.votes ,name="votes")
]

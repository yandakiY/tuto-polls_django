from django.urls import path
from . import views
# Link to my index function in views.py

app_name = 'polls'

urlpatterns = [
    # ex : /polls
    path("", views.index, name="index"),
    
    #ex : details : /polls/3
    path("<int:question_id>/" , views.details , name="details"),
    
    # ex results : /polls/3/results
    path("<int:question_id>/results", views.results , name="results"),
    
    # votes : /polls/3/votes
    path("<int:question_id>/votes" , views.votes ,name="votes")
]

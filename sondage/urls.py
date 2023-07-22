from django.urls import path
from . import views

app_name = "sondage"
urlpatterns = [
    path('' , views.IndexView.as_view() , name="index"),
    path('<int:pk>/' , views.QuestionDetailView.as_view() , name="details"),
    path('<int:pk>/results' , views.ResultView.as_view() , name="results"),
    path('<int:question_id>/votes' , views.votes , name="votes"),
    path('<int:question_id>/delete' , views.delete , name="delete"),
    path('add/' , views.AddQuestionView.as_view() , name="add"),
    # Add a new question in database
    path('saveQuestion' , views.addQuestion, name="saveQuestion")
]

from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from sondage.models import Question , Choice

# Create your views here.
class IndexView(generic.ListView):
    
    template_name = "sondage/index.html"
    context_object_name = "question_lists"
    
    
    def get_queryset(self) -> QuerySet[Any]:
        return Question.objects.all()
    

class QuestionDetailView(generic.DetailView):
    model = Question
    template_name = "sondage/details.html"

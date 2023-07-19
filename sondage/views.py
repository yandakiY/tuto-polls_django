from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from sondage.models import Question , Choice
from django.utils import timezone

# Create your views here.
class IndexView(generic.ListView):
    
    template_name = "sondage/index.html"
    context_object_name = "question_lists"
    
    
    def get_queryset(self) -> QuerySet[Any]:
        return Question.objects.all().exclude(choice__isnull=True).filter(date_pub__lte=timezone.now()).order_by('-date_pub')
    

class QuestionDetailView(generic.DetailView):
    model = Question
    template_name = "sondage/details.html"
    
    
class ResultView(generic.DetailView):
    # view the results of votes for each choice
    model = Question
    template_name = "sondage/results.html"

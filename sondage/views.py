from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render , get_object_or_404
from django.views import generic
from .models import Question , Choice
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
class IndexView(generic.ListView):
    
    template_name = "sondage/index.html"
    context_object_name = "question_lists"
    
    
    def get_queryset(self) -> QuerySet[Any]:
        return Question.objects.all().exclude(choice__isnull=True).filter(date_pub__lte=timezone.now()).order_by('-date_pub')
    

class QuestionDetailView(generic.DetailView):
    model = Question
    template_name = "sondage/details.html"
    
    
    def get_queryset(self) -> QuerySet[Any]:
        return Question.objects.filter(date_pub__lte=timezone.now())
    
    
class ResultView(generic.DetailView):
    # view the results of votes for each choice
    model = Question
    template_name = "sondage/results.html"
    
    
def votes(request , question_id):
    
    # get question who correspond to id
    question = get_object_or_404(Question , pk=question_id)
    
    # get the choice selected
    try:
        choice_selected = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError):
        # render view details sondage with ErrorMEssage
        return render(
            request, "sondage/details.html",{"question": question , "error_message":"Error, make a choice"}
        )
    else:
        choice_selected.votes += 1
        choice_selected.save()
        
        return HttpResponseRedirect(reverse("sondage:details" , args=(question_id,)))
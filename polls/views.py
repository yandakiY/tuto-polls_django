from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .models import Question , Choice
from django.template import loader
from django.shortcuts import render , get_object_or_404
from django.urls import reverse
from django.views import generic
# Create your views here.

# my first view in Django
# use now class with generic ListView for the View of my app
class IndexView(generic.ListView):
    # dont need of model
    # model = Question
    template_name = 'polls/index.html'
    context_object_name = 'join_elements'
    
    def get_queryset(self) -> QuerySet[Question]:
        return Question.objects.order_by('-date_pub')[:9]

# Details polls
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'

# Results polls (/polls/4/result)
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# Vote polls (/polls/5/votes)
def votes(request , question_id):
    
    # Get question correspond
    question = get_object_or_404(Question , pk = question_id)
    
    try:
        # choice selected
        choice_selected = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist): # Return message error
        return render(
            request,
            'polls/details.html',
            {'question':question, "error_message": "You didn't select a choice."}
        )
    else:
        choice_selected.votes += 1
        choice_selected.save()
        
        # Redirect with Httpresponseredirect
        return HttpResponseRedirect(reverse("polls:results" , args=(question.id,)))
    
    # return HttpResponse("Votes for polls %s"%question_id)
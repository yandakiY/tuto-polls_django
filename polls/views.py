from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .models import Question , Choice
from django.template import loader
from django.shortcuts import render , get_object_or_404
from django.urls import reverse
# Create your views here.

# my first view in Django
def index(request):
    # get the last 5 elements of Question
    last_elements = Question.objects.order_by('-date_pub')[:9]
    
    # element to send
    context = {'join_elements': last_elements}
    
    # return HttpResponse(loader_manager.render(context , request))
    return render(request , 'polls/index.html' , context)

# Details polls
def details(request , question_id):
    
    # get question who correspond to id (question_id)
    # question = Question.objects.get(pk = question_id)
    question = get_object_or_404(Question , pk = question_id)
    
    # call render function
    return render(request , 'polls/details.html' ,{'question': question})
    # return HttpResponse("Details Polls %s"%question_id)

# Results polls (/polls/4/result)
def results(request , question_id):
    
    # The goal here is to : display the question , these choices and the vote who correspond to the choice
    # Get id Question
    question = get_object_or_404(Question , pk = question_id)
    
    return render(request , 'polls/results.html' ,{'question':question})
    # return HttpResponse("Results for polls %s"%question_id)

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
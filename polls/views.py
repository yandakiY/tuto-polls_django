from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import render , get_object_or_404
# Create your views here.

# my first view in Django
def index(request):
    # get the last 5 elements of Question
    last_elements = Question.objects.order_by('-date_pub')[:9]
    
    # Join last 5 elements with ','
    # join_elements = ",".join([element.question_text for element in last_elements])
    
    # Call loader wih function get_template
    # loader_manager = loader.get_template('polls/index.html')
    
    # element to send
    context = {'join_elements': last_elements}
    
    # return HttpResponse(loader_manager.render(context , request))
    return render(request , 'polls/index.html' , context)

# Details polls
def details(request , question_id):
    
    # get question who correspond to id (question_id)
    # question = Question.objects.get(pk = question_id)
    question = get_object_or_404(Question , pk = question_id)
    
    # context
    context = {'question': question}
    
    # call render function
    return render(request , 'polls/details.html' ,context)
    # return HttpResponse("Details Polls %s"%question_id)

# Results polls (/polls/4/result)
def results(request , question_id):
    return HttpResponse("Results for polls %s"%question_id)

# Vote polls (/polls/5/votes)
def votes(request , question_id):
    return HttpResponse("Votes for polls %s"%question_id)
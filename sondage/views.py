from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render , get_object_or_404
from django.views import generic
from .models import Question , Choice
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
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
    
   
   
class AddQuestionView(generic.ListView):
    model = Question
    template_name = "sondage/add_sondage.html"


# Add a question in database
def addQuestion(request):
    print(request.POST['question_text'])
    print(request.POST['date_pub'])
    print(request.POST['nbvotes'])
    
    # create a question occurence
    new_question = Question(question_text=request.POST['question_text'] , date_pub=request.POST['date_pub'] , nbvotes=eval(request.POST['nbvotes']))
    # save this question
    new_question.save()
    
    # get the question save in database and add the choice who correspond
    # get the index
    indexLastQuestion = len(Question.objects.all()) - 1
    print('Last index' , indexLastQuestion)
    # return HttpResponseRedirect(reverse("sondage:add"))
    return HttpResponseRedirect(reverse("sondage:addChoice" , args=(indexLastQuestion,)))
    # pass


# Page view add a choice for a question
class addChoiceToQuestionView(generic.ListView):
    model = Question
    template_name = "sondage/add_choice.html"
    context_object_name = "question"
    # model
    
    def get_queryset(self):
        # index = self.request.GET.get('index')
        # print(index)
        # print(Question.objects.all()[len(Question.objects.all())-1].question_text)
        return Question.objects.all()[len(Question.objects.all())-1]
    

def savechoice(request , question_id):
    # get question 
    question = Question.objects.get(id = question_id)
    print("Question is :{}".format(question))
    # add choice now
    for x in range(question.nbvotes):
        print(request.POST['choice_text{}'.format(x+1)])
        question.choice_set.create(choice_text=request.POST['choice_text{}'.format(x+1)])
    
    # response redirect
    return HttpResponseRedirect(reverse("sondage:index" , args=()))

# Delete a question from Database
def delete(request , question_id):
    
    # get the question who correspond to id
    question = get_object_or_404(Question , pk=question_id)
    # delete this
    question.delete()
    # redirect to index.html
    return HttpResponseRedirect(reverse('sondage:index'))
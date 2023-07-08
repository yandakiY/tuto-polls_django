from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# my first view in Django
def index(request):
    return HttpResponse("Hello this my index page")
from django.urls import path
from . import views
# Link to my index function in views.py

urlpatterns = [
    path("", views.index, name="index")
]

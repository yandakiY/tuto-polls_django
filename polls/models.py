from django.db import models

# Create your models here.
# We have two models for polls apps : Question and Choice

class Question(models.Model):
    # Text question
    question_text = models.CharField(max_length=200)
    # Date publishing
    date_pub = models.DateTimeField("date published")
    

class Choice(models.Model):
    # foreign key
    question = models.ForeignKey(Question , on_delete=models.CASCADE)
    # title choice
    choice_text = models.CharField(max_length=200)
    # votes count
    votes = models.IntegerField(default=0)
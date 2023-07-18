from django.db import models
import datetime
from django.contrib import admin
from django.db.models import CharField
from django.utils import timezone


# Create your models here.
# We have two models for polls apps : Question and Choice

class Question(models.Model):
    
    
    # Text question
    question_text = models.CharField(max_length=200)
    # Date publishing
    date_pub = models.DateTimeField("date published")
    
   
    def __str__(self) -> str:
        return self.question_text
    
    
    @admin.display(
        boolean=True,
        ordering="-date_pub",
        description="Published recently"
    )
    
    def was_published_recently(self):
        """
        the publication date is between date time now and 1 day ago
        """
        # we check if value of date_pub is between this time now - datetime.timedelta(days=1)
        # determine timezone now()
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_pub <= now


class Choice(models.Model):
    # foreign key
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # title choice
    choice_text = models.CharField(max_length=200)
    # votes count
    votes = models.IntegerField(default=0)

    def __str__(self) -> CharField:
        return self.choice_text

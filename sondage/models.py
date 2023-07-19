from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Question(models.Model):
    # property
    question_text = models.CharField(max_length=200)
    date_pub = models.DateTimeField("Date of publiction")
    
    def is_recent(self):
        """Verify if the question is recent. A question recent is a question posted between yesterday and now"""
        now = timezone.now()
        
        return now - datetime.timedelta(days=1) <= self.date_pub <= now
    
    def __str__(self) -> str:
        return self.question_text

# Class Choice
class Choice(models.Model):
    # property
    question = models.ForeignKey(Question , on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

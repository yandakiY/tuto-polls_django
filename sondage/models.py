from django.db import models

# Create your models here.

class Question(models.Model):
    # property
    question_text = models.CharField(max_length=200)
    date_pub = models.DateTimeField("Date of publiction")
    
    
    
    def __str__(self) -> str:
        return self.question_text

# Class Choice
class Choice(models.Model):
    # property
    question = models.ForeignKey(Question , on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

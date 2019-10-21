from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Question(models.Model):
    #Fields
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    #Methods
    #Added to shwo question_text text readble when queying
    def __str__(self):
        return self.question_text
    # Method to reurtn the recent questions    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)    


class Choice(models.Model):
    #Fields
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    #Methods
    #Added to shwo choice text readble when queying
    def __str__(self):
        return self.choice_text
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
# After programming the classes we must migrate them with the following commands
# python3 manage.py makemigrations polls
# python3 manage.py migrate


class Question(models.Model):
    # id  I commend id because is not neccesary
    question_text = models.CharField(max_length=200)
    issue_date = models.DateTimeField("issue date")
    auto_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ': ' + self.question_text

    def was_published_recently(self):
        return self.issue_date >= timezone.now - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text

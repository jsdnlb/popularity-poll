from django.db import models

# Create your models here.
# After programming the classes we must migrate them with the following commands
# python3 manage.py makemigrations polls
# python3 manage.py migrate


class Question(models.Model):
    # id  I commend id because
    question_text = models.CharField(max_length=200)
    issue_date = models.DateTimeField("issue date")
    auto_date = models.DateTimeField(auto_now_add = True)


class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.


def index(request):
    latest_question_list = Question.objects.all()
    return render(request, 'polls/index.html', {
        'latest_question_list': latest_question_list
    })


def detail(request, question_id):
    return HttpResponse(f'You are looking question number {question_id}')


def result(request, question_id):
    return HttpResponse(f'You are looking result of the question number {question_id}')


def vote(request, question_id):
    return HttpResponse(f'You are voting question number {question_id}')

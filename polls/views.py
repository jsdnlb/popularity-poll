from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('You are on the main page Popularity Poll')

def detail(request, question_id):
    return HttpResponse(f'You are looking question number {question_id}')

def result(request, question_id):
    return HttpResponse(f'You are looking result of the question number {question_id}')

def vote(request, question_id):
    return HttpResponse(f'You are voting question number {question_id}')

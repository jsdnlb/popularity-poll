from ast import arg
from re import template
import django
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic import ListView
from .models import Question, Choice

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        # Return the last five published questions
        return Question.objects.order_by('-issue_date')[:5]
    
    pass


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'

class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

""" def index(request):
    latest_question_list = Question.objects.all()
    return render(request, 'polls/index.html', {
        'latest_question_list': latest_question_list
    })


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {
        'question': question
    })


def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html',{
        'question': question
    }) """


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': 'Dont choice answer'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))

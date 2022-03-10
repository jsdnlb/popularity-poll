from django.urls import path
# Import views from polls
from . import views

urlpatterns= [
    path('',views.index, name='index'),
    # ex: /polls/1
    path('<int:question_id>/',views.detail, name='index'),
    # ex: /polls/1/result
    path('<int:question_id>/result',views.result, name='index'),
    # ex: /polls/1/vote
    path('<int:question_id>/vote',views.vote, name='index')
]
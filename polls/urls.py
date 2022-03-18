from django.urls import path
# Import views from polls
from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/1
    path('<int:question_id>/detail/examples/dani/jsdnlb/',
         views.detail, name='detail'),
    # ex: /polls/1/result
    path('<int:question_id>/result', views.result, name='result'),
    # ex: /polls/1/vote
    path('<int:question_id>/vote', views.vote, name='vote')
]

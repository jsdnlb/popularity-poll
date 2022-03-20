from django.urls import path
# Import views from polls
from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/1
    path('<int:pk>/detail/examples/dani/jsdnlb/',
         views.DetailView.as_view(), name='detail'),
    # ex: /polls/1/result
    path('<int:pk>/result', views.ResultView.as_view(), name='result'),
    # ex: /polls/1/vote
    path('<int:question_id>/vote', views.vote, name='vote')
]

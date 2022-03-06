from django.urls import path
# Import views from polls
from . import views

urlpatterns= [
    path('',views.index, name='index')
]
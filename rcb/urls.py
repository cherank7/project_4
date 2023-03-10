from rcb.views import *
from django.urls import path
app_name='none'
urlpatterns=[
    path('kohli/',kohli,name='kohli'),
    path('abd/',abd,name='abd'),
    path('fans/',fans,name='fans'),
]
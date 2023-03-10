from csk.views import *
from django.urls import path
app_name='cric'
urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
    path('raina/',raina,name='raina'),
    path('jadeja/',jadeja,name='jadeja')
]
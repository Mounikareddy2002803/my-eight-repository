from django.urls import path
from app2.views import *
app_name='something2'

urlpatterns=[ 
    path('jinja_print1/',jinja_print1,name='jinja_print1')
]
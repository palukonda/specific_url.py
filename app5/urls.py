from django.urls import path
from app5.views import*
app_name='bluestar'
urlpatterns=[
    path('kgf/',kgf,name='kgf'),
]
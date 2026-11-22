from django.urls import path
from .views import *

urlpatterns = [
    path('asia/', Asia, name='asia'),
    path('europe/', Europe, name='europe'),
    path('australia/', Australia, name='australia'),
    path('canada/', Canada, name='canada'),
    path('africa/', Africa, name='africa'),
    path('about/', about, name='about'),
    path('read/<int:id>/', read, name='read'),
]
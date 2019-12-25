from django.shortcuts import render
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addNewEvent, name='addNewEvent'),
    path('events', views.listOfEvents, name='listOfEvents'),
    path('calendar', views.calendar, name='calendar'),
    path('settings', views.settings, name='settings'),
    path('<str:eventname>', views.viewEvent, name='viewEvent'),
    path('delete/<str:eventname>', views.deleteEvent, name='deleteEvent')
]
